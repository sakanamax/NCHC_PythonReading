#bs4 練習
from bs4 import BeautifulSoup
import requests

url = "http://www.timeanddate.com/weather/"

html = requests.get(url).text

sp = BeautifulSoup(html, "html.parser")
# print(sp)

# 找出 a 標籤
links = sp.find_all('a')

print(links[10])
print(links[10].contents)
print(links[10].get('href'))