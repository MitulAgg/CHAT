import uuid
# from app.manager.agent import question_answering_agent
from app.models.ChatResponse import ChatResponse
from app.models.ChatRequest import ChatRequest
from app.models.SessionRequest import SessionRequest as SessionRequest
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv
from typing import Dict
from fastapi import APIRouter, FastAPI
from ..services.test import run
from app.services.test import run as run_test
from app.services.test import clear as clear
import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from app.manager.agent import setup_rag_pipeline
from app.manager.agent import load_and_split_text, create_vector_store
load_dotenv()


router = APIRouter(tags=["chatbot"])

load_dotenv()

runner = None

@router.post("/chat/")
async def create_session(request : SessionRequest ):
    """
    Create a new chat session with the provided context as user preferences.
    
    Args:
        q: Initial context string to set as user preferences
        
    Returns:
        ChatResponse containing session_id and current session state
    """
    q= request.q
    if(request.url!=None):
        run_test(request.url)
    else:
        clear()

    with open(r"scraped_data.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content == "temp":
            print("No content found in the text file. Using Google Search tool instead.")
            question_answering_agent = LlmAgent(
                name="question_answering_agent",
                model="gemini-2.0-flash",
                description="Question answering agent using google search and user preferences",
                instruction="""
                You are a helpful assistant that answers questions about the user's preferences .
              
                Here is some information about the user's preferences:
                Preferences: 
                {user_preferences}
                """,
                tools=[google_search]
            )
        else:
            print("Content found in the text file. Using RAG tool for question answering.")
            file_path =r"scraped_data.txt"
            chunks = load_and_split_text(file_path)
            vector_store = create_vector_store(chunks)
            rag_tool = setup_rag_pipeline(vector_store)
            question_answering_agent = LlmAgent(
                name="question_answering_agent",
                model="gemini-2.0-flash",
                description="Question answering agent using RAG from a text file",
                instruction="""
                You are a helpful assistant that answers questions about the user's preferences and content from a text file.
                Use the RAG tool to retrieve relevant context and provide accurate answers.
                If the answer is not in the text or preferences, say so clearly.

                Here is some information about the user's preferences:
                Preferences: 
                {user_preferences}
                """,
                tools=[rag_tool]
            )



    APP_NAME = "chatbot"
    session_service_stateful = InMemorySessionService()
    global runner
    runner = Runner(
            agent=question_answering_agent,
            app_name=APP_NAME,
            session_service=session_service_stateful,
    )
    initial_state = {
         "user_preferences": q,
    }
    SESSION_ID = str(uuid.uuid4())
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id="default_user",  # You can replace this with a real user ID if needed
        session_id=SESSION_ID,
        state=initial_state,
    )

    return ChatResponse(
        session_id=SESSION_ID,
        response="Session created successfully. Please use the /chat/continue endpoint to send messages.",
        session_state=initial_state
    )

@router.post("/chat/continue")
async def continue_chat(request: ChatRequest):
    """
    Continue an existing chat session.
    
    Args:
        request: ChatRequest containing the message and session_id
        
    Returns:
        ChatResponse containing session_id, response, and current session state
    """

    

    user_content = types.Content(
            role="user", 
            parts=[types.Part(text=request.message)]
        )
    response_text = ""
    
    for event in runner.run(
        user_id="default_user",  # You can replace this with a real user ID if needed
        session_id=request.session_id,
        new_message=user_content,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text = event.content.parts[0].text
    return ChatResponse(
        session_id=request.session_id,
        response=response_text,
        session_state={}
    )
