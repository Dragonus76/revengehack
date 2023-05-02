import requests
import re
from bs4 import BeautifulSoup
from textblob import TextBlob

def get_social_data(user_id, access_token):
    url = f"https://api.socialnetwork.com/v1/{user_id}/?access_token={access_token}"
    response = requests.get(url)
    return response.json()

def extract_wealthy_names(article):
    blob = TextBlob(article)
    wealthy_names = set()

    for sentence in blob.sentences:
        if "billionaire" in sentence.lower() or "millionaire" in sentence.lower():
            names = re.findall(r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b', sentence.string)
            wealthy_names.update(names)
    return list(wealthy_names)

def search_target_articles(target_names, search_engine_api_key):
    url = "https://api.searchengine.com/v1/search"
    headers = {"apikey": search_engine_api_key}
    target_articles = []

    for name in target_names:
        params = {"q": name, "count": 10}
        response = requests.get(url, headers=headers, params=params)
        articles = response.json()["value"]

        for article in articles:
            article_data = {"title": article["name"], "url": article["url"]}
            target_articles.append(article_data)

    return target_articles

def sort_results(results):
    return sorted(results, key=lambda x: x["net_worth"], reverse=True)
