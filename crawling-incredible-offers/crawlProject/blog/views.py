from django.shortcuts import render
from blog.crawling import Products

url = "https://www.digikala.com/incredible-offers/"
def getproduct(request):
    pr = Products(url)
    products = pr.get_product()
    zipped = zip(products[0], products[1], products[2])
    return render(request, 'products/index.html',{'products_list': zipped})
# Create your views here.
