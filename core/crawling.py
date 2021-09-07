import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

url1 = "https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fAuction"
url = "https://lostark.game.onstove.com/Auction"

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

driver.get(url1)
driver.find_element_by_name('user_id').send_keys('killdog070@naver.com')
driver.find_element_by_name('user_pwd').send_keys('songjm8138')
login_x_path = '//*[@id="idLogin"]/div[3]/button'
driver.find_element_by_xpath(login_x_path).click()

try:
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'btnSearch')))
    html_source = driver.page_source
    print(html_source)
except:
    print('fail')





