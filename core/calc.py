import time
from itertools import product
import itertools
import pickle
import tqdm
import pandas as pd
import numpy as np
from pyarrow import csv

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


def calc(input_engraving, bonus, stone):
    temp_engraving={}
    for i in input_engraving:
        if i[1] == 3: temp_engraving[i[0]] = 15
        elif i[1] == 2: temp_engraving[i[0]] = 10
        else: i[1] = temp_engraving[i[0]] = 5

    for i in bonus:
        temp_engraving[i[0]] -= i[1]
    for i in stone[:2]:
        temp_engraving[i[0]] -= i[1]
    temp_engraving = {key: val for key, val in temp_engraving.items() if val > 0}

    print(temp_engraving)
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

    # accessories_combination = x

    accessories_combination.sort()
    accessories_combination = list(set(map(tuple, accessories_combination)))
    accessories_pair = list(set(itertools.chain.from_iterable(accessories_combination)))
    accessories_kind = list(set(itertools.chain.from_iterable(accessories_pair)))
    return accessories_combination, accessories_pair, accessories_kind


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


def calc_ac1(ac_com, ac_kind, nature, stone):
    ac_pro_list = []
    permut_com = []
    for com in ac_com:
        for imp0, imp1, imp2, imp3, imp4 in itertools.permutations(com):
            permut_com.append(((nature[0], imp0), (nature[1], imp1), (nature[2], imp2), (nature[3], imp3), (nature[4], imp4)))

    permut_com = list(set(permut_com))
    print(permut_com[0])
    print(permut_com[1])
    print(len(permut_com))
    # ((('목걸이', ('신속', '특화')), (('전문의', 3), ('중갑 착용', 3))), (('귀걸이', ('신속', '')), (('임시', 0), ('중갑 착용', 4))), (('귀걸이', ('신속', '')), (('전문의', 3), ('중갑 착용', 5))), (('반지', ('신속', '')), (('각성', 3), ('전문의', 3))), (('반지', ('신속', '')), (('각성', 5), ('중갑 착용', 3))))

    imprint_kind = [x[0]for x in ac_kind]
    df_itemlist = pd.read_csv('./data/item_list.csv')

    count = 1
    total = len(permut_com)
    for parts in permut_com:
        pair_ac_list = []
        for part in parts:
            ac_type = part[0][0]
            nature_name = part[0][1][0]
            effect1_name = part[1][0][0]
            effect1_value = part[1][0][1]
            effect2_name = part[1][1][0]
            effect2_value = part[1][1][1]

            condition1 = (df_itemlist['name'].str.split(' ').str[-1] == ac_type)
            condition2 = (df_itemlist['nature1_name'] == nature_name) | (df_itemlist['nature2_name'] == nature_name)
            if effect1_name == '임시':
                condition3 = (df_itemlist['effect1_name'] == effect2_name) & (df_itemlist['effect1_value'] == effect2_value) & ~(df_itemlist['effect2_name'].isin(imprint_kind))
                condition4 = (df_itemlist['effect2_name'] == effect2_name) & (df_itemlist['effect2_value'] == effect2_value) & ~(df_itemlist['effect1_name'].isin(imprint_kind))
            elif effect2_name == '임시':
                condition3 = (df_itemlist['effect1_name'] == effect1_name) & (df_itemlist['effect1_value'] == effect1_value) & ~(df_itemlist['effect2_name'].isin(imprint_kind))
                condition4 = (df_itemlist['effect2_name'] == effect1_name) & (df_itemlist['effect2_value'] == effect1_value) & ~(df_itemlist['effect1_name'].isin(imprint_kind))
            else:
                condition3 = (df_itemlist['effect1_name'] == effect1_name) & (df_itemlist['effect1_value'] == effect1_value) & (df_itemlist['effect2_name'] == effect2_name) & (df_itemlist['effect2_value'] == effect2_value)
                condition4 = (df_itemlist['effect2_name'] == effect1_name) & (df_itemlist['effect2_value'] == effect1_value) & (df_itemlist['effect1_name'] == effect2_name) & (df_itemlist['effect1_value'] == effect2_value)
            ac_list = df_itemlist.loc[condition1 & condition2 & (condition3 | condition4)]
            ac_list = ac_list.fillna('')
            ac_list = tuple(map(tuple, ac_list.to_numpy()))
            pair_ac_list.append(ac_list)
            del ac_list

        print('{0}/{1}\tstart\t{2}'.format(count, total, [y for x, y in parts]))
        temp_product = list(product(*pair_ac_list))
        del pair_ac_list
        for acs in temp_product:
            if acs[0][13] == 0 or acs[1][13] == 0 or acs[2][13] == 0 or acs[3][13] == 0 or acs[4][13] == 0:     # 즉시 구매 불가능한 매물
                continue
            if acs[1][0] == acs[2][0] or acs[3][0] == acs[4][0]:    # 이름 중복 체크
                continue
            effect = {'공격력 감소': 0, '공격속도 감소': 0, '방어력 감소': 0, '이동속도 감소': 0, stone[2][0]: stone[2][1]}   # 디버프 체크
            for ac in acs:
                effect[ac[5]] += ac[6]
            if max(effect.values()) >= 5:
                continue
            acs_set = tuple(set(acs))
            ac_pro_list.append(acs_set)

        print('finish {0}'.format(len(ac_pro_list)))
        count += 1

    ac_pro_list = list(set(ac_pro_list))
    for i in range(len(ac_pro_list)):
        sort_aclist = tuple(sorted(ac_pro_list[i], key=lambda x: (len(x[0].split()[-1]), x[0].split()[-1]), reverse=True))
        price_total = (sum([x[13] for x in sort_aclist]))
        nature_total = {sort_aclist[0][7]: 0, sort_aclist[0][9]: 0}
        ac1, ac2, ac3, ac4, ac5 = sort_aclist[0], sort_aclist[1], sort_aclist[2], sort_aclist[3], sort_aclist[4]
        nature_total[ac1[7]] += ac1[8]
        nature_total[ac1[9]] += ac1[10]
        nature_total[ac2[7]] += ac2[8]
        nature_total[ac3[7]] += ac3[8]
        nature_total[ac4[7]] += ac4[8]
        nature_total[ac5[7]] += ac5[8]
        nature_sum = sum(list(nature_total.values()))
        nature_total = list(nature_total.items())
        # nature_total = '[{0} {1}][{2} {3}]'.format(nature_total[0][0], nature_total[0][1], nature_total[1][0], int(nature_total[1][1]))

        ac_pro_list[i] = (price_total, nature_sum, nature_total, ac1, ac2, ac3, ac4, ac5)



    columns = ['price_total', 'nature_sum', 'nature_total', 'ac1', 'ac2', 'ac3', 'ac4', 'ac5']
    df_result = pd.DataFrame(ac_pro_list, columns=columns)
    df_result.to_csv('./data/result.csv', index=False)


def calc_ac(ac_com, item_list, nature_list, stone):
    ac_list = []
    for com in ac_com:
        part_com = itertools.permutations(com)
        for parts in part_com:
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
                effect = {'공격력 감소': 0, '공격속도 감소': 0, '방어력 감소': 0, '이동속도 감소': 0, stone[2][0]: stone[2][1]}
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

    with open("./data/ac_list.pkl", "wb") as fw:
        pickle.dump(ac_list, fw)


def filtering():
    df_itemlist = csv.read_csv('./data/result.csv').to_pandas()
    print(type(df_itemlist))
    df_itemlist = df_itemlist.sort_values(by='price_total')
    print(df_itemlist.head(5))
    print(df_itemlist.tail(5))

    # nature_sum = 1950
    #
    #
    # condition1 = (df_itemlist['name'].str.split(' ').str[-1] == ac_type)
    # condition2 = (df_itemlist['nature1_name'] == nature_name) | (df_itemlist['nature2_name'] == nature_name)
    # ac_list = df_itemlist.loc[condition1 & condition2 & (condition3 | condition4)]




    # with open("ac_list.pkl", "rb") as fr:
    #     ac_list = pickle.load(fr)
    # temp_list = [i for i in ac_list if i[1]['특화']>=1465]
    #
    # temp_list.sort(key=lambda x:x[0])
    # j=0
    # for i in temp_list:
    #     k=[x['quality'] for x in i[2]]
    #     if k[0] <= 89: continue
    #     print(k, i)
    #     if j > 100: break
    #     j+=1
    # print(len(temp_list))
