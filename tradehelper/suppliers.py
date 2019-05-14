import random

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
    random_goods = sum_roll_dee_six(1)
    print(f'This supplier has {random_goods} available. They are:')
    for x in range(random_goods):
        random_item = combine_dee_six(2)
        print(f'Item {random_item}')

goods_available()

#bedtime thoughts... I could return a string for goods_available, and then set up a dict with each D66 roll for each good,
#which would allow me to return what actual good is returned.