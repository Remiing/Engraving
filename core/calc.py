from itertools import product
import itertools


def calc(engraving_value, bonus, stone):
    temp_engraving = engraving_value

    for key in bonus:
        temp_engraving[key] -= bonus[key]
    for key in stone:
        temp_engraving[key] -= stone[key]

    engraving_name = []
    engraving_num = []
    for key, val in engraving_value.items():
        engraving_name.append(key)
        engraving_num.append(val)

    engraving_combination = combination(engraving_num)

    engraving_product = list(product(*engraving_combination))

    for item in engraving_product[:]:
        item_array = sum(item, [])
        if len(item_array) != 10:
            engraving_product.remove(item)
            continue
        if item_array.count(4) + item_array.count(5) > 5:
            engraving_product.remove(item)

    list1 = []
    list2 = []
    for engraving_item in engraving_product:
        num1 = []
        num2 = []
        for name, num in zip(engraving_name, engraving_item):

            for i in num:
                temp_engraving = {}
                if i > 3:
                    temp_engraving[name] = i
                    num1.append(temp_engraving)
                else:
                    temp_engraving[name] = i
                    num2.append(temp_engraving)
        list1.append(num1)
        list2.append(num2)

    list_up = []
    list_down = []
    for i in range(len(list1)):
        if len(list1[i]) < 5:
            select_engraving = list(itertools.combinations(list2[i], 5-len(list1[i])))
            for move_engraving_tuple in select_engraving:
                move_engraving_list = list(move_engraving_tuple)
                list_up.append(list1[i]+move_engraving_list)
                remain_engraving_list = list2[i][:]
                for x in move_engraving_list:
                    remain_engraving_list.remove(x)
                list_down.append(remain_engraving_list)
        else:
            list_up.append(list1[i])
            list_down.append(list2[i])


    # accessories combination
    accessories_combination = []
    for up, down in zip(list_up, list_down):
        down_permutation = list(itertools.permutations(down, 5))
        for x in list(down_permutation):
            accessorie = []
            breaker = False
            for a, b in zip(up, x):
                temp_dict = a.copy()
                temp_dict.update(b)
                if len(temp_dict) != 2:
                    breaker = True
                    break
                temp_dict = sorted(temp_dict.items())
                accessorie.append(tuple(temp_dict))
            if breaker == True:
                continue

            accessorie.sort()
            accessories_combination.append(accessorie)

    accessories_combination.sort()
    accessories_combination = set(list(map(tuple, accessories_combination)))

    for i in accessories_combination:
        print(i)
    print(len(accessories_combination))





def combination(engraving_num):
    combination_dict = {15: [[5, 5, 5], [5, 4, 3, 3], [4, 4, 4, 3], [3, 3, 3, 3, 3]],
                        14: [[5, 3, 3, 3], [4, 4, 3, 3], [5, 5, 4]],
                        13: [[5, 5, 3], [4, 3, 3, 3], [5, 4, 4]],
                        12: [[5, 4, 3], [3, 3, 3, 3], [4, 4, 4]],
                        11: [[5, 3, 3], [4, 4, 3]],
                        10: [[5, 5], [4, 3, 3]],
                        9: [[5, 4], [3, 3, 3]],
                        8: [[5, 3], [4, 4]],
                        7: [[4, 3]],
                        6: [[3, 3]],
                        5: [[5]],
                        4: [[4]],
                        3: [[3]]}

    combination_list = []
    for i in engraving_num:
        combination_list.append(combination_dict[i])

    return combination_list


if __name__ == "__main__":
    engraving_value = {'원한': 15, '슈퍼 차지': 15, '잔재된 기운': 15, '기습의 대가': 15, '저주받은 인형': 15}
    bonus = {'슈퍼 차지': 12, '잔재된 기운': 12}
    stone = {'원한': 7, '기습의 대가': 8}

    engraving_value = {'원한': 15, '예리한 둔기': 15, '절정': 15, '돌격 대장': 15, '저주받은 인형': 15}
    bonus = {'돌격 대장': 9, '절정': 12}
    stone = {'원한': 5, '예리한 둔기': 9}

    calc(engraving_value, bonus, stone)
