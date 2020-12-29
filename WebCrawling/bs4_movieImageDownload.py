import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)  #content가 이미지
        
        if idx >= 4:
            break