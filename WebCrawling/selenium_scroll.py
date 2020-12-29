from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤(자바스크립트로)
# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")  #1920 x 1080 (한페이지 내리기)

#화면 가장 아래로 스크롤 내리기
# 높이가 변하지 않을 때까지 스크롤 내리기
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "   할인되지 않은 영화 제외")
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
print("==============================")
print()
