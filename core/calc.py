def calc(engraving_value, bonus, stone):
    temp_engraving = engraving_value
    for key in bonus:
        temp_engraving[key] -= bonus[key]
    for key in stone:
        temp_engraving[key] -= stone[key]
    print(temp_engraving)




if __name__ == "__main__":
    engraving_value = {'원한': 15, '슈퍼 차지': 15, '잔재된 기운': 15, '기습의 대가': 15, '저주받은 인형': 15}
    bonus = {'저주받은 인형': 9, '잔재된 기운': 12}
    stone = {'원한': 7, '기습의 대가': 8}
    calc(engraving_value, bonus, stone)
