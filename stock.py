from bs4 import BeautifulSoup
import requests

# url = "http://www.pawnshop-assistant.com/pawnshop_inventory"
url = "https://www.w3schools.com"
web_data = requests.get(url)
web_data.encoding = "utf-8"

soup = BeautifulSoup(web_data.text,'html.parser')
print(soup.find_all('title'))