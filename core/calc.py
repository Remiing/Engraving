from itertools import product
import itertools
import pickle
import tqdm


def calc(input_engraving, bonus, stone):
    temp_engraving = input_engraving

    for key in bonus:
        temp_engraving[key] -= bonus[key]
    for key in stone[0]:
        temp_engraving[key] -= stone[0][key]
    #print(temp_engraving)
    # {'원한': 10, '예리한 둔기': 6, '절정': 3, '돌격 대장': 6}

    engraving_name = []
    engraving_num = []
    for key, val in temp_engraving.items():
        engraving_name.append(key)
        engraving_num.append(val)
    #print(engraving_name)
    #print(engraving_num)
    # ['원한', '예리한 둔기', '절정', '돌격 대장']
    # [10, 6, 3, 6]

    engraving_combination = combination(engraving_num)
    #print(engraving_combination)
    # [[[5, 5], [4, 3, 3]], [[3, 3]], [[3]], [[3, 3]]]

    engraving_product = list(product(*engraving_combination))
    #print(engraving_product)
    # [([5, 5], [3, 3], [3], [3, 3]), ([4, 3, 3], [3, 3], [3], [3, 3])]

    for item in engraving_product[:]:
        item_array = sum(item, [])
        if len(item_array) > 10:
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

        count = len(num1) + len(num2)
        if count < 10:
            for i in range(10-count):
                num2.append({'임시': 0})
        list1.append(num1)
        list2.append(num2)
    #print(list1)
    #print(list2)
    # [[{'원한': 5}, {'원한': 5}], [{'원한': 4}]]
    # [[{'예리한 둔기': 3}, {'예리한 둔기': 3}, {'절정': 3}, {'돌격 대장': 3}, {'돌격 대장': 3}, {'임시': 0}, {'임시': 0}, {'임시': 0}], [{'원한': 3}, {'원한': 3}, {'예리한 둔기': 3}, {'예리한 둔기': 3}, {'절정': 3}, {'돌격 대장': 3}, {'돌격 대장': 3}, {'임시': 0}, {'임시': 0}]]

    list_up = []
    list_down = []
    for i in range(len(list1)):
        if len(list1[i]) < 5:
            select_engraving = list(itertools.combinations(list2[i], 5-len(list1[i])))
            #print(select_engraving)
            #print(len(select_engraving))
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


    x = [i for i in accessories_combination if (('버스트', 3), ('원한', 5)) in i]

    accessories_combination = x

    accessories_combination.sort()
    accessories_combination = list(set(map(tuple, accessories_combination)))
    arr = list(set(itertools.chain.from_iterable(accessories_combination)))
    #print(arr)

    return accessories_combination, arr


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


def calc_ac(ac_com, item_list, nature_list, stone):
    ac_list = []
    for com in tqdm.tqdm(ac_com):
        if not (('버스트', 3), ('원한', 5)) in com:
            continue
        part_com = itertools.permutations(com)
        for parts in part_com:
            if not parts[1]==(('버스트', 3), ('원한', 5)) or parts[2]==(('버스트', 3), ('원한', 5)):
                continue
            # print(parts)
            part_list = []
            for engraving_option, nature in zip(parts, nature_list):
                part = nature[0]
                nature_option = nature[1]
                engraving_option1 = engraving_option[0]
                engraving_option2 = engraving_option[1]
                nature_name = nature_option[0] + nature_option[1]
                engraving_name = engraving_option1[0] + '_' + str(engraving_option1[1]) + '&' + engraving_option2[0] + '_' + str(engraving_option2[1])
                part_list.append(item_list[part][nature_name][engraving_name])
                # print(part, nature_name, engraving_name)
                # print(item_list[part][nature_name][engraving_name])

            temp_list = list(product(*part_list))
            for ac in temp_list:
                if ac[1]['name'] == ac[2]['name'] or ac[3]['name'] == ac[4]['name']:
                    continue
                effect = {'공격력 감소': 0, '공격속도 감소': 0, '방어력 감소': 0, '이동속도 감소': 0, stone[1][0]: stone[1][1]}
                for i in ac:
                    effect[i['effect'][2][0]] = effect[i['effect'][2][0]] + i['effect'][2][1]
                for i in effect.values():
                    if i >= 5:
                        break
                else:
                    total = 0
                    nature_total = {ac[0]['nature'][0][0]: 0, ac[0]['nature'][1][0]: 0}
                    for i in ac:
                        total += int(i['buy_price'])
                        for j in i['nature']:
                            nature_total[j[0]] += j[1]
                    ac_list.append((total, nature_total, ac))
                    #print(ac)

    with open("ac_list.pkl", "wb") as fw:
        pickle.dump(ac_list, fw)


def minn():
    with open("ac_list.pkl", "rb") as fr:
        ac_list = pickle.load(fr)
    temp_list = [i for i in ac_list if i[1]['특화']>=1465]

    temp_list.sort(key=lambda x:x[0])
    j=0
    for i in temp_list:
        k=[x['quality'] for x in i[2]]
        if k[0] <= 89: continue
        print(k, i)
        if j > 100: break
        j+=1
    print(len(temp_list))
