from bs4 import BeautifulSoup
import requests

def getBillBoard100():
    res=requests.get('https://www.billboard.com/charts/hot-100/')
    if res.ok:
        pass