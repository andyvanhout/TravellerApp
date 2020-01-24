import random

def one_dee_six():
    return random.randint(1,6)

def roll_dee_six(number):
    diceroll = 0
    for i in range(number):
        diceroll += one_dee_six()
    return diceroll

def ice_core_density(modifier):
    density_chart = {
        6: 0.3,
        7: 0.4,
        8: 0.4,
        9: 0.4,
        10: 0.4,
        11: 0.5,
        12: 0.5,
        13: 0.5,
        14: 0.5,
        15: 0.6,
        16: 0.6,
        17: 0.6,
        18: 0.7
    }
    density_result = roll_dee_six(3) + modifier
    if density_result <= 6:
        return density_chart[6]
    elif density_result >= 18:
        return density_chart[18]
    else:
        return density_chart[density_result]