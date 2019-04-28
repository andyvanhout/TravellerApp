import random

def roll_dee_six(number):
    result = []
    for i in range(number):
        result.append(random.randint(1,6))
    #print(f'Dice rolled:{result}')
    #print("Total: ", sum(result))
    return sum(result)

def passenger_traffic(dice_modifier):
    result = roll_dee_six(2) + dice_modifier
    #print(f'Passenger Traffic Roll: {result}')
    if (result >= 20):
        return roll_dee_six(10)
    elif (result == 19):
        return roll_dee_six(9)
    elif (result == 18):
        return roll_dee_six(8)
    elif (result == 17):
        return roll_dee_six(7)
    elif (result == 16):
        return roll_dee_six(6)
    elif (result == 15 or result == 14):
        return roll_dee_six(5)
    elif (result == 13 or result == 12 or result == 11):
        return roll_dee_six(4)
    elif (result <= 10 and result >= 7):
        return roll_dee_six(3)
    elif (result <= 6 and result >= 4):
        return roll_dee_six(2)
    elif (result == 3 or result == 2):
        return roll_dee_six(1)
    else:
        return 0

def freight_traffic(dice_modifier):
    result = roll_dee_six(2) + dice_modifier
    #print(f'Freight Traffic Roll: {result}')
    if (result >= 20):
        return roll_dee_six(10)
    elif (result == 19):
        return roll_dee_six(9)
    elif (result == 18):
        return roll_dee_six(8)
    elif (result == 17):
        return roll_dee_six(7)
    elif (result == 16 or result == 15):
        return roll_dee_six(6)
    elif (result == 14 or result == 13 or result == 12):
        return roll_dee_six(5)
    elif (result <= 11 and result >= 9):
        return roll_dee_six(4)
    elif (result <= 8 and result >= 6):
        return roll_dee_six(3)
    elif (result == 5 or result == 4):
        return roll_dee_six(2)
    elif (result == 3 or result == 2):
        return roll_dee_six(1)
    else:
        return 0