from utils.request_utils import headers

def processUrl(completeUrl):
    req = requests.get(completeUrl, headers = headers)
    soup = bs(req.text, 'lxml')
    articles = soup.find("main",{"class":"listing-items"}).find_all("article", attrs={"data-element-id": True})
    housesIDs = [article.get("data-element-id") for article in articles]
    previousHousesIDs = getHouses()
    cleanHouses()
    updateNewHouses(housesIDs)
    return req