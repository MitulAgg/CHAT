import uuid
from app.manager.agent import question_answering_agent
from app.models.ChatResponse import ChatResponse
from app.models.ChatRequest import ChatRequest
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv
from typing import Dict
from fastapi import APIRouter, FastAPI


router = APIRouter(tags=["chatbot"])

load_dotenv()

APP_NAME = "chatbot"
session_service_stateful = InMemorySessionService()
runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
)

@router.get("/chat/")
async def create_session(q: str):
    """
    Create a new chat session with the provided context as user preferences.
    
    Args:
        q: Initial context string to set as user preferences
        
    Returns:
        ChatResponse containing session_id and current session state
    """
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

    response_text=""
    user_content = types.Content(
        role="user", parts=[types.Part(text=request.message)]
    )
    
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
