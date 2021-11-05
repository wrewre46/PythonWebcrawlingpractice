from bs4 import BeautifulSoup

page = open('sample.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

#문서에 있는 p태그를 전부 찾기
print(soup.find_all('p'))

#문서에 있는 p태그 하나만 찾기
print(soup.find('p'))

#<p class='outer-text'> 만 가지고 오기
print(soup.find_all('p', class_='outer-text'))

# id가 first인것을 다 가져오기
print(soup.find_all(id='first'))

#첫번째 p 태그를 발견하면 안에 있는 내용만 가져오기
print(soup.find('p').get_text())

#p 태그 안에 있는 내용만 가져오기
for tag in soup.find_all('p'):
    print(tag.get_text())