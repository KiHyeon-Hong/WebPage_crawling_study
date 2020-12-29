import re

p = re.compile("ca.e")
# . : 하나의 문자를 의미
# ^(^de) : 문자열의 시작을 의미, desk, destination....
# $(se$) : 문자열의 끝을 의미, case, base...

m = p.match("case")

if m:
    print(m.group())
else:
    print("매칭되지 않음")

# match의 동작은 처음부터 일치하는지 확인이므로 매칭이 되는 부분 출력

m = p.search("good care")
# 주어진 문자열 중에 일치하는게 있는지 확인
print(m.group())

# group 일치하는 문자열 반환 care
# string 문자열 그대로 반환 careless
# m.start 일치하는 문자열의 시작 index 0
# m.end 일치하는 문자열의 끝 index 4
# span 일치하는 문자열의 시작과 끝의 index (0, 4)

lst = p.findall("good care cafe")
# findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 정규식을 사용할때
# p = re.compile("원하는 형태")
# m = p.match("비교할 문자열") // 주어진 문자열의 처음부터 확인
# lst = p.findall("비교할 문자열") // 일치하는 모든 것을 리스트 반환