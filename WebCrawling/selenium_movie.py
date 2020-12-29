import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}
url = "https://play.google.com/store/movies/top"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

#with open("movie.html", "w", encoding="utf8") as f:
#    #f.write(res.text)
#    f.write(soup.prettify())

# 접속 사용자에 따라 언어가 달라진다

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# 스크롤에 따라 로딩이 된다
# 동적 페이징이다
# 최초 10개만 보임

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

