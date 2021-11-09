from bs4 import BeautifulSoup
import requests
import mechanize
import unicodedata

url = "http://www.pawnshop-assistant.com/pawnshop_inventory"
br = mechanize.Browser()
br.open(url)

br.select_form(nr=0)
br.form.controls[0]._value = 'stock1'
br.form.controls[1]._value = 'stock1'
br.submit()

cookies = {'PHPSESSID':'dldifgovcfpe4h6iiitsa46m24'} 

data = requests.get('http://www.pawnshop-assistant.com/pawnshop_inventoryoverview', cookies=cookies)


data.encoding = 'utf-8'
soup =  BeautifulSoup(data.text, 'html.parser')

find = soup.find_all('a')

with open('data.txt', 'w') as f:
    for i in find:
        f.write(str(i.text))
        f.write('\n')

find = soup.find_all('a')

# count = 0
# for i in find:
#     count = count + 1
#     print(i.text)
# print(count)

# findName = soup.find_all('td',{'class':''})
# findDetail = soup.find_all('td',{'class':'c'})

# for i in findName:
#     print(i.text)

# for i in findDetail:
#     print(i.text)
