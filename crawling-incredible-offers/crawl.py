import lxml
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get

url = "https://www.digikala.com/incredible-offers/"
class Products(object):

    def __init__(self, url):
                 super(Products, self).__init__()
                 page = get(url)
                 self.soup = BeautifulSoup(page.content, 'lxml')

    def content(self):
                 content = self.soup.find(id="main")
                 return content.find_all("div", class_="c-product-list__item js-product-list-content")

    