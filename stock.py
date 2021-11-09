from bs4 import BeautifulSoup
import requests
import mechanize
import unicodedata

url = "http://www.pawnshop-assistant.com/pawnshop_inventory"
# url = "https://www.w3schools.com"
# web_data = requests.get(url)
# web_data.encoding = "utf-8"

# soup = BeautifulSoup(web_data.text,'html.parser')
# print(soup.find_all('title'))
br = mechanize.Browser()
br.open(url)

br.select_form(nr=0)
br.form.controls[0]._value = 'stock1'
br.form.controls[1]._value = 'stock1'
br.submit()
# print(br.response().read().decode(encoding='utf-8'))

cookies = {'PHPSESSID': 'narv5siuvgfrojeck8r5lq5kk5'}
payload = {'prefix': 'filter', 'goto_page': 1, 'per_page': 50, 'javascript_function': 'pagechange', 'filter_status': '-', 'filter_current_page': 1}
data = requests.post('http://www.pawnshop-assistant.com/ajaxfunctions/getInventoryList', cookies=cookies, data=payload)
# print(data.text.encode('iso-8859-1').decode('utf-8'))

data.encoding = 'utf-8'
soup =  BeautifulSoup(data.text, 'html.parser')
findName = soup.find_all('td',{'class':''})
findDetail = soup.find_all('td',{'class':'c'})

for i in findName:
    print(i.text)

for i in findDetail:
    print(i.text)
