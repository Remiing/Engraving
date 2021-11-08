import requests
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from collections import defaultdict
from webdriver_manager.chrome import ChromeDriverManager


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))


def access():
    url = "https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fAuction"
    # url = "https://lostark.game.onstove.com/Auction"
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # access auction
    driver.get(url)
    driver.find_element_by_name('user_id').send_keys('killdog070@naver.com')
    driver.find_element_by_name('user_pwd').send_keys('songjm8138')
    login_x_path = '//*[@id="idLogin"]/div[3]/button'
    driver.find_element_by_xpath(login_x_path).click()
    try:
        WebDriverWait(driver, 300).until(expected_conditions.element_to_be_clickable((By.ID, 'btnSearch')))
        html_source = driver.page_source
        #print(html_source)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        #return driver
    except:
        print('fail')


def make_session():
    session = requests.Session()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    #print(cookies)
    for cookie in cookies:
        c = {cookie['name']: cookie['value']}
        session.cookies.update(c)
    return session


def crawling(session, ac, nature):
    url = 'https://lostark.game.onstove.com/Auction/GetAuctionListV2'
    category = {
        '목걸이': 200010,
        '귀걸이': 200020,
        '반지': 200030
    }
    grade_list = {
        '유물': 5,
        '고대':6
    }
    nature_list = {
        '치명': 15,
        '특화': 16,
        '제압': 17,
        '신속': 18,
        '인내': 19,
        '숙련': 20,
        '': ''
    }
    engraving_list = {
        '각성': 255,
        '갈증': 286,
        '강령술': 243,
        '강화 무기': 129,
        '강화 방패': 242,
        '결투의 대가': 288,
        '고독한 기사': 225,
        '광기': 125,
        '광전사의 비기': 188,
        '구슬동자': 134,
        '굳은 의지': 123,
        '극의: 체술': 190,
        '급소 타격': 142,
        '기습의 대가': 249,
        '긴급구조': 302,
        '넘치는 교감': 199,
        '달의 소리': 287,
        '달인의 저력': 238,
        '돌격대장': 254,
        '두 번째 동료': 258,
        '마나 효율 증가': 168,
        '마나의 흐름': 251,
        '멈출 수 없는 충동': 281,
        '바리케이드': 253,
        '버스트': 279,
        '번개의 분노': 246,
        '부러진 뼈': 245,
        '분노의 망치': 196,
        '분쇄의 주먹': 236,
        '불굴': 235,
        '사냥의 시간': 290,
        '상급 소환사': 198,
        '선수필승': 244,
        '세맥타통': 256,
        '속전속결': 300,
        '슈퍼 차지': 121,
        '승부사': 248,
        '시선 집중': 298,
        '실드 관통': 237,
        '심판자': 282,
        '아드레날린': 299,
        '아르데타인의 기술': 284,
        '안정된 상태': 111,
        '약자 무시': 107,
        '에테르 포식자': 110,
        '여신의 가호': 239,
        '역천지체': 257,
        '예리한 둔기': 141,
        '오의 강화': 127,
        '오의난무': 292,
        '완벽한 억제': 280,
        '원한': 118,
        '위기 모면': 140,
        '일격필살': 291,
        '잔재된 기운': 278,
        '저주받은 인형': 247,
        '전문의': 301,
        '전투 태세': 224,
        '절실한 구원': 195,
        '절정': 276,
        '절제': 277,
        '점화': 293,
        '정기 흡수': 109,
        '정밀 단도': 303,
        '죽음의 습격': 259,
        '중갑 착용': 240,
        '중력 수련': 197,
        '진실된 용맹': 194,
        '진화의 유산': 285,
        '질량 증가': 295,
        '초심': 189,
        '최대 마나 증가': 167,
        '추진력': 296,
        '축복의 오라': 283,
        '충격 단련': 191,
        '타격의 대가': 297,
        '탈출의 명수': 202,
        '포격 강화': 193,
        '폭발물 전문가': 241,
        '피스메이커': 289,
        '핸드거너': 192,
        '화력 강화': 130,
        '환류': 294,
        '황제의 칙령': 201,
        '황후의 은총': 200
    }

    item_list = nested_dict(3, dict)
    for engraving_option1, engraving_option2 in ac:
        for part, nature_option in nature:
            temp_list = []
            page = 1
            while True:
                data = {
                    'request[firstCategory]': 200000,
                    'request[secondCategory]': category[part],
                    'request[itemTier]': 3,
                    'request[itemGrade]': 5,
                    'request[itemLevelMin]': 0,
                    'request[itemLevelMax]': 1700,
                    'request[gradeQuality]': '',
                    'request[etcOptionList][0][firstOption]': 3,
                    'request[etcOptionList][0][secondOption]': engraving_list[engraving_option1[0]],
                    'request[etcOptionList][0][minValue]': engraving_option1[1],
                    'request[etcOptionList][0][maxValue]': engraving_option1[1],
                    'request[etcOptionList][1][firstOption]': 3,
                    'request[etcOptionList][1][secondOption]': engraving_list[engraving_option2[0]],
                    'request[etcOptionList][1][minValue]': engraving_option2[1],
                    'request[etcOptionList][1][maxValue]': engraving_option2[1],
                    'request[etcOptionList][2][firstOption]': 2,
                    'request[etcOptionList][2][secondOption]': nature_list[nature_option[0]],
                    'request[etcOptionList][2][minValue]': '',
                    'request[etcOptionList][2][maxValue]': '',
                    'request[etcOptionList][3][firstOption]': 2,
                    'request[etcOptionList][3][secondOption]': nature_list[nature_option[1]],
                    'request[etcOptionList][3][minValue]': '',
                    'request[etcOptionList][3][maxValue]': '',
                    'request[pageNo]': page,
                    'request[sortOption][Sort]': 'BIDSTART_PRICE',
                    'request[sortOption][IsDesc]': 'false'
                }
                print(page, part, engraving_option1, engraving_option2, nature_option)
                response = session.post(url, data=data)
                soup = BeautifulSoup(response.text, "html.parser")
                if not soup.select('.empty'):
                    temp_list.append(parsing(soup))
                    page += 1
                else:
                    nature_name = nature_option[0] + nature_option[1]
                    engraving_name = engraving_option1[0] + '_' + str(engraving_option1[1]) + '&' + engraving_option2[0] + '_' + str(engraving_option2[1])
                    item_list[part][nature_name][engraving_name]=temp_list
                    break



def parsing(soup):
    item_list = []
    for item in soup.select('#auctionListTbody > tr'):
        if not item: break
        name = item.select_one('#auctionListTbody > tr > td > div.grade > span.name').text
        effect = []
        for ef in item.select('#auctionListTbody > tr > td > div.effect > ul:nth-child(1) > li'):
            option_text = ef.text
            effect.append((option_text[option_text.index('[') + 1:option_text.index(']')], int(option_text[option_text.index('+') + 1])))
        nature_temp = item.select_one('#auctionListTbody > tr > td > div.effect > ul:nth-child(2) > li').text
        nature = (nature_temp[nature_temp.index('[') + 1:nature_temp.index(']')], int(nature_temp[nature_temp.index('+') + 1:]))
        quality = item.select_one('#auctionListTbody > tr > td:nth-child(3) > div > span.txt').text
        start_price = item.select_one('#auctionListTbody > tr > td:nth-child(5) > div > em').text
        buy_price = item.select_one('#auctionListTbody > tr > td:nth-child(6) > div > em').text.replace(' ', '').replace('\n', '').replace('\r', '')
        item_info = {'name': name, 'effect': effect, 'nature': nature, 'quality': quality, 'start_price': start_price, 'buy_price': buy_price}
        item_list.append(item_info)

    return item_list




if __name__ == "__main__":
    #driver = access()
    session = make_session()
    crawling(session)












