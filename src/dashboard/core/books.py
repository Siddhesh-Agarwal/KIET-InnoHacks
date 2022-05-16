# recommend random book based on genre
# parse goodreads.com to get a random book
# use BS4
import requests
from bs4 import BeautifulSoup
from random import choice


def random_book(genre: str):
    """
    Returns a random book from the specified genre.
    """
    genre = genre.lower()
    url = f"https://www.goodreads.com/genre/{ genre.replace(' ', '-') }"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    book = soup.find("div", class_="coverWrapper", recursive=True)
    img = book.find("img")["src"]
    name = book.find("img")["alt"]
    return img, name
