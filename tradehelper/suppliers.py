import random
import modules.trade_goods as tg

def roll_dee_six(number):
    result = []
    for i in range(number):
        result.append(random.randint(1,6))
    return result

def sum_roll_dee_six(number):
    dice_list = roll_dee_six(number)
    return sum(dice_list)

def combine_dee_six(number):
    combined_dice = roll_dee_six(number)
    combined_string = ''.join(map(str, combined_dice))
    return int(combined_string)

def goods_available():
    trade_codes = input("Input Trade Codes: ")
    trade_code_list = trade_codes.split(' ')
    trade_set = []
    
    for code in trade_code_list: 
        trade_set.extend(tg.trade_codes[code])
    trade_list = []
    for key in set(trade_set):
        trade_list.append(tg.trade_goods[key])
    trade_list.sort()
    for item in trade_list:
        print(item)

def random_goods():
    random_goods = sum_roll_dee_six(1)
    print(f'\nThis supplier has {random_goods} available. They are:')
    for number in range(random_goods):
        random_item = combine_dee_six(2)
        print(tg.trade_goods[str(random_item)])

goods_available()
random_goods()