import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "http://nadocoding.tistory.com"
res = requests.get(url, headers=headers)
res.raise_for_status()

print("웹 스크래핑을 진행합니다")


with open("nado.html", "w", encoding="utf-8") as f:
    f.write(res.text)

# user agent string 검색 후 what is my user agent?
# https://www.whatismybrowser.com/detect/what-is-my-user-agent

