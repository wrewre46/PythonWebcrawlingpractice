from bs4 import BeautifulSoup
import re
doc = ['<html><head><title>Page title</title></head>', \
    '<body><p id="firstpara" align="center">This is paragraph <b>one</b></p>', \
    '<p id="secondpara" align="blah">This is a paragraph <b>two</b></p>', '</html>']

soup = BeautifulSoup(''.join(doc), 'html.parser')

#태그를 정렬해서 보여주기
# print(soup.prettify())

# #b로 시작하는 태그 출력하기
# tagsStartingWithB = soup.find_all(re.compile('^b'))
# print([tag.name for tag in tagsStartingWithB])

#print(soup.find_all(['title','p']))

#태그의 속성이 2개인것을 출력
#print(soup.find_all(lambda tag:len(tag.attrs)==2))

#태그중에 align속성이 "center"인 경우만 검색합니다. 
# print(soup.find_all(align="center"))

#태그의 id속성이 para로 끝나는 경우만 검색합니다. 
# print(soup.find_all(id=re.compile("para$")))

#다시 간단한 HTML소스를 생성해서 class속성을 통해 검색합니다. 
soup =BeautifulSoup("""
    Bob's<b>Bold</b>Barbeque Sauce now available 
    <b class="hickory">Hickory</b> and <b class="lime">Lime</a>
    """, "html.parser")

#<b>태그 중에 class=lime이라고 되어 있는 태그를 검색합니다. 
print(soup.find("b", {"class":"lime"}).get_text())