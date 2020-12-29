from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#기다리기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.maximize_window()

browser.get("https://flight.naver.com/flights/")

browser.find_element_by_link_text("가는날 선택").click()

#이번달 27 28일 선택
#browser.find_elements_by_link_text("30")[0].click()
#browser.find_elements_by_link_text("31")[0].click()

browser.find_elements_by_link_text("30")[0].click()
browser.find_elements_by_link_text("31")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색

browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과 출력(로딩 때매 사긴이 지연된다)
# 1. 몇초를 기다리는 방식 -> 단점 언제 끝나는지 모름
# 2. 그 도중에 끝나면 동작을 처리해!

#elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")

# element가 나올때까지 10초간 기다리는데...
# xpath외에도 id, class_name, link_text 등 사용 가능합니다
#10 초 안에 나오면 진행하는데 그것이 xpath조건으로 해당하는 값이 나올때까지 기다려줘
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    #browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
    print(elem[0].text)
finally:
    browser.quit()
