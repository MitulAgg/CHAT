Chatbot RAG & Google GenAI Integration

A FastAPI-based chatbot application that dynamically switches between a Google Search tool and a Retrieval-Augmented Generation (RAG) pipeline using LangChain. It allows scraping user-provided URLs for context, storing embeddings in a vector store, and answering user queries through a Google Gemini-based LLM agent.

🚀 Features

Dynamic Context Loading: Scrape web pages via a URL or clear previous context

RAG Pipeline: Leverages LangChain’s Chroma vector store and HuggingFace embeddings for Retrieval-Augmented Generation

Google GenAI Integration: Uses Google’s Gemini models (gemini-1.5-flash / gemini-2.0-flash) through the ADK Runner and LlmAgent

Session Management: In-memory session service to track user conversations

FastAPI Endpoints:

POST /chat/ to create a new session with user preferences or URL context

POST /chat/continue to continue the chat flow

Environment Configuration with dotenv

🛠️ Tech Stack

Backend: Python 3.9+ | FastAPI

GenAI SDK: google-genai, google-adk

Web Scraping: requests, beautifulsoup4

RAG & Embeddings: LangChain, Chroma, HuggingFace Embeddings

Session Store: InMemorySessionService

Environment: python-dotenv

📦 Installation & Setup

Clone the repository

git clone https://github.com/MitulAgg/CHAT.git
cd CHAT

Create & activate a virtual environment

python -m venv venv
source venv/bin/activate   # Unix
venv\\Scripts\\activate  # Windows

Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

Set environment variables Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key_here


Run the application

uvicorn app.main:app --reload

The API will be available at http://127.0.0.1:8000



