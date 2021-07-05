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

    def product(self):
                 products = self.content()
                 product_info = {}
                 all_products = []

                 for product in products:

                          product_info['product_name'] = product.find("div", class_="c-product-box__img js-url js-snt-carousel_product")["title"]
                          product_info['new_price'] = product.find("div", class_="c-price__value-wrapper js-product-card-price").text

                          try: 
                              product_info['discount'] = product.find("div", class_="c-price__discount-oval").find("span").text
                          except:
                              product_info['discount'] = "Check out the discount" 

                          all_products.append(product_info)  

                 return all_products                                      

             





pr = Products(url)

print(pr.product())

