#!/usr/bin/python3
import requests
import pickle
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(100000)


def down(
        url:
        str = 'https://www.kaoyany.top/search.php?CateID=&q=%E5%BC%A0%E5%AE%87'
):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def save(text, fileName: str = 'html.pickle'):
    file = open(fileName, 'wb')
    pickle.dump(text, file)
    file.close


def load(fileName: str = 'html.pickle'):
    soup = None
    try:
        with open(fileName, 'rb') as file:
            soup = pickle.load(file)
    finally:
        return soup


if __name__ == "__main__":
    soup = load()
    if not soup:
        soup = down()
        save(soup)

    print(soup)
    pass
