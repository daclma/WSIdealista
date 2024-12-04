import requests
from bs4 import BeautifulSoup as bs
from utils.headers import HEADERS

def scrape_houses_from_url(url):
    req = requests.get(url, headers=HEADERS)
    if req.status_code != 200:
        raise Exception(f"Error calling url: {url}")
    
    soup = bs(req.text, "lxml")
    articles = soup.find("main", {"class": "listing-items"}).find_all("article", attrs={"data-element-id": True})
    houses_ids = [article.get("data-element-id") for article in articles]
    return houses_ids
