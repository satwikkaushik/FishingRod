import requests
from bs4 import BeautifulSoup

def extract(url):
    # checking format of URL
    if("https://" not in url):
        url = "https://" + url

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
