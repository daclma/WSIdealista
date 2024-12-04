from model.houses import Houses
from service.scraping_service import scrape_houses_from_url
from db import db

def get_houses():
    return Houses.query.all()

def clean_houses():
    Houses.query.delete()
    db.session.commit()

def update_new_houses(houses_ids):
    for house_id in houses_ids:
        house = Houses(house_id=int(house_id))
        db.session.add(house)
    db.session.commit()

def compare_houses(houses_ids, previous_houses):
    #Convert housesIDs from Strings to Integer
    houses_ids_set = set(int(house_id) for house_id in houses_ids)
    #Get houses ids from data model object
    previous_houses_set = set(house.house_id for house in previous_houses)
    #With this, you can remove the houses in the first List, that are present in the previous list, so you only get the new houses.
    new_houses = houses_ids_set - previous_houses_set
    return list(new_houses)

def process_houses(url):
    houses_ids = scrape_houses_from_url(url)
    previous_houses = get_houses()
    new_houses = compare_houses(houses_ids, previous_houses)
    clean_houses()
    update_new_houses(houses_ids)

    if new_houses:
        new_houses_with_url = [f"Nou pis! URL: https://www.idealista.com/inmueble/{house_id}" for house_id in new_houses]
    else:
        new_houses_with_url = f"No hi ha cap pis nou :("

    return new_houses_with_url