from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.get("http://naver.com")

#elem = browser.find_element_by_class_name("link_login")
#elem.click()
# browser.back()
# browser.forward()
# borwser.refresh()
#browser.back()

#elem = browser.find_element_by_id("query")
#elem.send_keys("TearMoon")
#elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")    #1개
elem = browser.find_elements_by_tag_name("a")   #여러개

#for e in elem:
#    e.get_attribute("href")

browser.get("http://daum.net")

elem = browser.find_element_by_name("q")
elem.send_keys("TearMoon")
#elem.send_keys(Keys.ENTER)

# copy xpath
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

#browser.close()    #현재탭 닫기
browser.quit() #전체 닫기