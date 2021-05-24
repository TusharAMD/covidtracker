import requests
from bs4 import BeautifulSoup
quote_page = 'file:///E:/Full%20stack/Eyantra/Location/index.html'
page = requests.get(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('p')