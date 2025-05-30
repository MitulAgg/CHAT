from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize FastAPI app
app = FastAPI(title="ChatBot API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Simple in-memory session store
sessions = {}

# Pydantic model for request body
class ChatRequest(BaseModel):
    message: str
    session_id: str

# Pydantic model for response
class ChatResponse(BaseModel):
    session_id: str
    response: str
    session_state: dict

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Using gemini-1.5-flash as a substitute
    system_instruction="You are a helpful assistant that answers questions based on the user's preferences."
)

@app.get("/chat/")
async def create_session(q: str):
    """
    Create a new chat session with the provided context as user preferences.
    
    Args:
        q: Initial context string to set as user preferences
        
    Returns:
        ChatResponse containing session_id and current session state
    """

    # Create new session
    session_id = str(uuid.uuid4())
    print(f"Creating session with ID: {session_id} and preferences: {q}")
    initial_state = {
        "user_preferences": q,
        "chat_history": []
    }
    
    # Store session
    sessions[session_id] = initial_state
    
    return ChatResponse(
        session_id=session_id,
        response="Session created successfully. Please use the /chat/continue endpoint to send messages.",
        session_state=initial_state
    )

@app.post("/chat/continue")
async def continue_chat(request: ChatRequest):
    """
    Continue an existing chat session.
    
    Args:
        request: ChatRequest containing the message and session_id
        
    Returns:
        ChatResponse containing session_id, response, and current session state
    """
    # Verify session exists
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[request.session_id]
    
    # Prepare prompt with preferences and chat history
    prompt = f"""
    User Preferences: {session['user_preferences']}
    
    Chat History:
    {chr(10).join([f"User: {msg['user']}\nAssistant: {msg['assistant']}" for msg in session['chat_history']])}
    
    User: {request.message}
    """
    
    # Generate response
    response = model.generate_content(prompt)
    response_text = response.text.strip()
    
    # Update session history
    session['chat_history'].append({
        "user": request.message,
        "assistant": response_text
    })
    
    return ChatResponse(
        session_id=request.session_id,
        response=response_text,
        session_state=session
    )
