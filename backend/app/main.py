from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chatbot import router as chatbot_router
from google.adk.agents import Agent
from google.adk.tools import google_search
# from crewai_tools import ScrapeWebsiteTool
# from bs4 import BeautifulSoup

# def run():
#         try:
#             response = requests.get("https://en.wikipedia.org/wiki/Artificial_intelligence")
#             response.raise_for_status()
#             soup = BeautifulSoup(response.text, 'html.parser')
#             print("h1")
#             return soup.get_text()
#         except Exception as e:
#             print("here")
#             return f"Error scraping : {str(e)}"
# print(run)

app = FastAPI()
app.include_router(chatbot_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
