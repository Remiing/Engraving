import time
import requests
import pickle
import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from collections import defaultdict
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np


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
    # driver.get(url)
    # driver.find_element_by_name('user_id').send_keys('')
    # driver.find_element_by_name('user_pwd').send_keys('')
    # login_x_path = '//*[@id="idLogin"]/div[4]/button/span'
    # driver.find_element_by_xpath(login_x_path).click()
    try:
        WebDriverWait(driver, 300).until(expected_conditions.element_to_be_clickable((By.ID, 'btnSearch')))
        html_source = driver.page_source
        #print(html_source)
        with open("./data/cookies.pkl", "wb") as fw:
            pickle.dump(driver.get_cookies(), fw)
        #return driver
    except:
        print('fail')


def make_session():
    session = requests.Session()
    with open("./data/cookies.pkl", "rb") as fr:
        cookies = pickle.load(fr)
    #print(cookies)
    for cookie in cookies:
        c = {cookie['name']: cookie['value']}
        session.cookies.update(c)
    return session


def crawling(session, ac, nature, quality):
    url = 'https://lostark.game.onstove.com/Auction/GetAuctionListV2'
    category = {
        '목걸이': 200010,
        '귀걸이': 200020,
        '반지': 200030
    }
    grade_list = {
        '유물': 5,
        '고대': 6
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
        '임시': '',
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
        '만개': 306,
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
        '황후의 은총': 200,
        '회귀': 306
    }
    columns = ['name', 'effect1_name', 'effect1_value', 'effect2_name', 'effect2_value', 'effect3_name', 'effect3_value', 'nature1_name', 'nature1_value', 'nature2_name', 'nature2_value', 'quality', 'start_price', 'buy_price']
    df_itemlist = pd.DataFrame(columns=columns)
    search_list = []
    for engraving_option1, engraving_option2 in ac:
        for i, j in zip(nature, quality):
            part = i[0]
            nature_option = i[1]
            qual = j
            search_list.append((part, engraving_option1, engraving_option2, nature_option, qual))
    search_list = list(set(search_list))  # 중복 제거
    for i in search_list:
        print(i)
    print(len(search_list))

    count = 1
    total = len(search_list)
    ac_total = 0
    for option in search_list:
        ac_list = []
        page = 1
        while True:
            if page > 1:
                break
            data = {
                'request[firstCategory]': 200000,
                'request[secondCategory]': category[option[0]],
                'request[itemTier]': 3,
                'request[itemGrade]': 5,
                'request[itemLevelMin]': 0,
                'request[itemLevelMax]': 1700,
                'request[gradeQuality]': option[4],
                'request[etcOptionList][0][firstOption]': 3,
                'request[etcOptionList][0][secondOption]': engraving_list[option[1][0]],
                'request[etcOptionList][0][minValue]': option[1][1],
                'request[etcOptionList][0][maxValue]': option[1][1],
                'request[etcOptionList][1][firstOption]': 3,
                'request[etcOptionList][1][secondOption]': engraving_list[option[2][0]],
                'request[etcOptionList][1][minValue]': option[2][1],
                'request[etcOptionList][1][maxValue]': option[2][1],
                'request[etcOptionList][2][firstOption]': 2,
                'request[etcOptionList][2][secondOption]': nature_list[option[3][0]],
                'request[etcOptionList][2][minValue]': '',
                'request[etcOptionList][2][maxValue]': '',
                'request[etcOptionList][3][firstOption]': 2,
                'request[etcOptionList][3][secondOption]': nature_list[option[3][1]],
                'request[etcOptionList][3][minValue]': '',
                'request[etcOptionList][3][maxValue]': '',
                'request[pageNo]': page,
                'request[sortOption][Sort]': 'BIDSTART_PRICE',
                'request[sortOption][IsDesc]': 'false'
            }
            time.sleep(6)
            response = session.post(url, data=data)
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.select('.empty'):
                break
            ac_list.extend(parsing(soup))
            page += 1
        df_temp = pd.DataFrame(ac_list, columns=columns)
        df_itemlist = pd.concat([df_itemlist, df_temp], ignore_index=True)
        print('{0}/{1}\t{2}\t{3}{4}\t[{5} {6}][{7} {8}] {9}'.format(count, total, option[0], option[3][0], option[3][1], option[1][0], option[1][1], option[2][0], option[2][1], len(ac_list)))
        print(ac_list)
        count += 1
        ac_total += len(ac_list)

    df_itemlist.to_csv('./data/item_list.csv', index=False)
    print(ac_total)



def parsing(soup):
    item_list = []
    for item in soup.select('#auctionListTbody > tr'):
        if not item: break
        item_info = []
        quality = int(item.select_one('#auctionListTbody > tr > td:nth-child(3) > div > span.txt').text)
        name = item.select_one('#auctionListTbody > tr > td > div.grade > span.name').text # name
        effect = []
        for i in item.select('#auctionListTbody > tr > td > div.effect > ul:nth-child(1) > li'):
            option_text = i.text
            effect.extend([option_text[option_text.index('[') + 1:option_text.index(']')], int(option_text[option_text.index('+') + 1])])
        nature = []
        nature_temp = item.select('#auctionListTbody > tr > td > div.effect > ul:nth-child(2) > li')
        for i in nature_temp:
            nature_text = i.text
            nature.extend([nature_text[nature_text.index('[') + 1:nature_text.index(']')], int(nature_text[nature_text.index('+') + 1:])])
        if len(nature) < 4:
            nature.extend(['', ''])
        start_price = int(item.select_one('#auctionListTbody > tr > td:nth-child(5) > div > em').text.replace(',', '')) # start price
        buy_price = item.select_one('#auctionListTbody > tr > td:nth-child(6) > div > em').text.replace(' ', '').replace('\n', '').replace('\r', '').replace(',', '') # buy_price
        if not buy_price.isdecimal():
            buy_price = 0
        else:
            buy_price = int(buy_price)
        # type = name.split(' ')[-1]

        # item_info.append(type)
        item_info.append(name)
        item_info.extend(effect)
        item_info.extend(nature)
        item_info.append(quality)
        item_info.append(start_price)
        item_info.append(buy_price)

        item_list.append(item_info)

    return item_list

