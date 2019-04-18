import random

def sum_two_dee_six():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    return dice_one + dice_two

def roll_size():
    return sum_two_dee_six() - 2

def roll_atmosphere(planet_size):
    
    unusual_chance = random.randint(0,100)
    
    if (planet_size == 0 or planet_size == 1):
        return 0
    elif (unusual_chance == 0 or unusual_chance == 100):
        return 15
    else:
        number = (sum_two_dee_six() - 7 + planet_size)
        if number < 0:
            return 0
        elif number > 15:
            return 15
        else:
            return number

def roll_hydrographics(planet_size, planet_atmosphere):
    
    if (planet_size == 0 or planet_size == 1):
        return 0
    elif (planet_atmosphere == 0 or planet_atmosphere == 1 or planet_atmosphere == 10 or planet_atmosphere == 11 or planet_atmosphere == 12):
        number = sum_two_dee_six() - 11 + planet_atmosphere
        if number < 0:
            return 0
        elif number > 10:
            return 10
        else:
            return number
    else:
        number = (sum_two_dee_six() - 7 + planet_atmosphere)
        if number < 0:
            return 0
        elif number > 10:
            return 10
        else:
            return number


def roll_temperature(planet_atmosphere):

    if (planet_atmosphere == 0 or planet_atmosphere == 1):
        return "Wildly Variable"
    elif (planet_atmosphere == 2 or planet_atmosphere == 3):
        return sum_two_dee_six() - 2
    elif (planet_atmosphere == 4 or planet_atmosphere == 5 or planet_atmosphere == 14):
        return sum_two_dee_six() - 1
    elif (planet_atmosphere == 6 or planet_atmosphere == 7):
        return sum_two_dee_six()
    elif (planet_atmosphere == 8 or planet_atmosphere == 9):
        return sum_two_dee_six() + 1
    elif (planet_atmosphere == 10 or planet_atmosphere == 13 or planet_atmosphere == 15):
        return sum_two_dee_six() + 2
    else:
        return sum_two_dee_six() + 6

def roll_population():
    pass