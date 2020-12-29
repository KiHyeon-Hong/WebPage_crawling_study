import requests
res = requests.get("http://google.com")
res.raise_for_status()

print("웹 스크래핑을 진행합니다")

print(len(res.text))

with open("myGoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)