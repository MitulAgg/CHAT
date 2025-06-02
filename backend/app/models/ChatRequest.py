from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str
    url : str | None = None  # Optional URL for web scraping if needed