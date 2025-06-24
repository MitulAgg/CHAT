from pydantic import BaseModel

class SessionRequest(BaseModel):
    q : str
    url: str | None = None  # Optional URL for web scraping if needed