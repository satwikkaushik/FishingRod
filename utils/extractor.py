import requests
from bs4 import BeautifulSoup
import re

def format_URL(url):
    if("https://" not in url):
        url = "https://" + url

    return url

def extract_URL(url):
    url = format_URL(url)

    try:
        # fetching HTML content of the page
        response = requests.get(url)

        # check for response status, auto generates exception if not 200
        response.raise_for_status()

        # parsing HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return links
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return []

def extract_content(url):
    url = format_URL(url)

    try:
        # fetching HTML content of the page
        response = requests.get(url)

        # check for response status, auto generates exception if not 200
        response.raise_for_status()

        # parsing HTML contents
        parsed_text = BeautifulSoup(response.text, 'html.parser')

        for a_tag in parsed_text.find_all('a'):
            a_tag.unwrap()  # removing <a> tag but keeping the text inside

        # extracting text
        text_content = parsed_text.get_text(separator='\n').strip()
        text_content = re.sub(r'\n+', '\n', text_content).strip()

        return text_content

    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return ""