import lxml
import re
import pandas as pd
from bs4 import BeautifulSoup
from requests import get

class Products(object):

    def __init__(self, url):
                 super(Products, self).__init__()
                 page = get(url)
                 self.soup = BeautifulSoup(page.content, 'lxml')

    def content(self):
                 content = self.soup.find(id="main")
                 return content.find_all("div", class_="c-product-list__item js-product-list-content")

    def get_product(self):
                 products = self.content()
                 product_name = []
                 price = []
                 discount = []

                 for product in products:
                          try:
                              product_name.append(product.find("div", class_="c-product-box__img js-url js-snt-carousel_product").find('img')["alt"])
                          except:
                              product_name.append("No name")
                       
                          try:
                              price.append(re.sub(r'\s+', ' ',product.find("div", class_="c-price__value-wrapper js-product-card-price").text))
                          except:
                              price.append("No Price")

                          try: 
                              discount.append(product.find("div", class_="c-price__discount-oval").find("span").text)

                          except:
                              discount.append("بدون تخفیف")

                    
                          df = pd.DataFrame({'Product Name':product_name,'Price':price,'Discount':discount}) 
                          df.to_csv('products.csv', index=False, encoding='utf-8-sig')
                          all_products = [product_name, price, discount]

                 return all_products                                      

             

