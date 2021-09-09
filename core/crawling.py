import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


def access():
    url = "https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fAuction"
    # url = "https://lostark.game.onstove.com/Auction"
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

    # access auction
    driver.get(url)
    driver.find_element_by_name('user_id').send_keys('killdog070@naver.com')
    driver.find_element_by_name('user_pwd').send_keys('songjm8138')
    login_x_path = '//*[@id="idLogin"]/div[3]/button'
    driver.find_element_by_xpath(login_x_path).click()
    try:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'btnSearch')))
        html_source = driver.page_source
        #print(html_source)
        return driver
    except:
        print('fail')


def search(driver):
    # click option button
    option_button = '//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[2]/form/fieldset/div/div[5]/button[2]'
    driver.find_element_by_xpath(option_button).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'lui-modal__search')))

    # insert item option
    driver.find_element_by_xpath(
        '//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div').click()
    driver.find_element_by_xpath(
        '//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div/div[2]/label[4]').click()

    # click search button
    search_button = '//*[@id="modal-deal-option"]/div/div/div[2]/button[1]'
    driver.find_element_by_xpath(search_button).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.invisibility_of_element((By.CLASS_NAME, 'lui-modal__search')))

    # crawl item list
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item_list = soup.select('#auctionListTbody > tr')
    print(item_list)

    time.sleep(999)

def run(self):
    '''
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

        # access auction
        driver.get(url)
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
        '''

    '''
        # click option button
        option_button = '//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[2]/form/fieldset/div/div[5]/button[2]'
        driver.find_element_by_xpath(option_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'lui-modal__search')))

        # insert item option
        driver.find_element_by_xpath('//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div').click()
        driver.find_element_by_xpath('//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div/div[2]/label[4]').click()

        # click search button
        search_button = '//*[@id="modal-deal-option"]/div/div/div[2]/button[1]'
        driver.find_element_by_xpath(search_button).click()
        '''


if __name__ == "__main__":
    driver = access()
    search(driver)












