from google.adk.agents import LlmAgent
from google.adk.tools import google_search
# from crewai_tools import WebsiteSearchTool
# from bs4 import BeautifulSoup

# def webScrapper(url):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Get text and clean it
#             scraped_text = soup.get_text()
            
#             # Remove extra whitespace and empty lines
#             cleaned_text = '\n'.join(
#                 line.strip() for line in scraped_text.splitlines() 
#                 if line.strip()  # Keep only non-empty lines
#             )
            
#             return cleaned_text
            
#         except Exception as e:
#             return f"Error scraping : {str(e)}"
# print(run)
# Create the root agent
# def run(url):
#     try:
#         response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         scraped_text = soup.get_text()
#         scraped_text = '\n'.join(
#                 line.strip() for line in scraped_text.splitlines() 
#                 if line.strip()  # Keep only non-empty lines
#             )
#         print(scraped_text)
#         with open('scraped_data.txt', 'w', encoding='utf-8') as file:
#             file.write(scraped_text)
#         return scraped_text
#     except Exception as e:
#         error_message = f"Error scraping: {str(e)}"
#         print(error_message)
#         return error_message

question_answering_agent = LlmAgent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user's preferences:
    Preferences: 
    {user_preferences}
    """,
    tools=[google_search]
)

# scrape_tool_instance = WebsiteSearchTool()

# # Wrap it with CrewaiTool for ADK compatibility
# adk_scrape_tool = CrewaiTool(
#     name="WebsiteScraper",
#     description="Scrapes the content of a provided URL to extract text for answering questions.",
#     tool=scrape_tool_instance
# )

# question_answering_agent= Agent(
#     name="web_scrape_agent",
#     model="gemini-2.0-flash",
#     instruction="""You are an assistant that answers questions based on the content of a webpage. 
#     When given a URL and a question, use the WebsiteScraper tool to scrape the content of the URL, 
#     then use that content as context to answer the question accurately. 
#     If the URL cannot be scraped or the content doesn't contain the answer, 
#     state that the information is not available.
#     url="https://en.wikipedia.org/wiki/Artificial_intelligence",
#     Here is some information about the user's preferences:
#      Preferences: 
#      {user_preferences}
#     """,
#     description="Answers questions by scraping content from a provided URL.",
#     tools=[adk_scrape_tool]
# )
