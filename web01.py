import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://www.naver.com')
soup = BeautifulSoup(page, 'html.parser')
#<span> 태그를 검색
print(soup.find_all("span"))