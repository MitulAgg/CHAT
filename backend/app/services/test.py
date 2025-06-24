import requests
from bs4 import BeautifulSoup

def run(url):
    print(url)
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        scraped_text = soup.get_text()
        scraped_text = '\n'.join(
                line.strip() for line in scraped_text.splitlines() 
                if line.strip()  # Keep only non-empty lines
            )
        # print(scraped_text)
        with open('scraped_data.txt', 'w', encoding='utf-8') as file:
            file.write(scraped_text)
        return scraped_text
    except Exception as e:
        error_message = f"Error scraping: {str(e)}"
        print(error_message)
        return error_message
def clear():
    """
    Clear the scraped data file.
    """
    with open('scraped_data.txt', 'w', encoding='utf-8') as file:
        file.write("temp")  # Clear the file content
    # print("Scraped data cleared.")
# run("https://en.wikipedia.org/wiki/Artificial_intelligence")
# clear()