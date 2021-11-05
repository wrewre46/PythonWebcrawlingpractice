import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen('https://www.naver.com')

soup = BeautifulSoup(data, 'html.parser')

list = soup.find_all('span', attrs={'class':"_1syGnXOL _3di88A4c"})

for item in list:
    try:
        title = item.find('strong').get_text()
        print(title.strip())
    except:
        pass
