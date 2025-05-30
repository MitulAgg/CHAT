from pydantic import BaseModel
from typing import Dict

class ChatResponse(BaseModel):
    session_id: str
    response: str
    session_state: dict