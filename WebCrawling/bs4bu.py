import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # 첫번째로 나온 a 태그 발견하면 뿌려줘
#print(soup.a.attrs) # 정보를 전부 뿌려줄 수 있다(dict 형태로 나온다)
#print(soup.a["href"]) # attrs에서 원하는 것 하나만 출력한다

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# 처음 발견되는값 가져온다

print(soup.find(attrs={"class":"Nbtn_upload"}))
# 이 페이지에서는 Nbtn_upload가 1개니까 둘 다 같은 값 나온다
# class="Nbtn_upload"인 <a> element를 찾아줘

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print()

# 부모와 자식 가능하다 soup에서...
print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling)  #개행 등으로.. 2번 할수도
rank3 = rank1.next_sibling.next_sibling.next_sibling.next_sibling
print(rank3.a.get_text())

print("============================")
print()

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print("============================")
print()
# 부모로 가기
#print(rank1.parent)

print("============================")
print()

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank1 = rank2.find_previous_sibling("li")
print(rank1.a.get_text())

print("============================")
print()

ranks = rank1.find_next_siblings("li")
print(ranks)

print("============================")
print()

webtoon = soup.find("a", text="여신강림-137화")
print(webtoon)