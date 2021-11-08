from core import crawling, calc


if __name__ == '__main__':
    engraving_value = {'원한': 15, '아드레날린': 15, '버스트': 15, '기습의 대가': 15, '저주받은 인형': 15}
    bonus = {'저주받은 인형': 12, '아드레날린': 9}
    stone = {'원한': 7, '기습의 대가': 8}
    nature = [('목걸이', ('치명', '특화')), ('귀걸이', ('치명', '')), ('귀걸이', ('치명', '')), ('반지', ('치명', '')), ('반지', ('치명', ''))]
    #quality = [50, 50, 50, 50, 50]

    ac_com, ac_kind = calc.calc(engraving_value, bonus, stone)
    #crawling.access()
    session = crawling.make_session()
    d = crawling.crawling(session, ac_kind, nature)


