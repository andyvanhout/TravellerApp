import random

def numbers_to_letters(number):
    if number == 10:
        return "A"
    if number == 11:
        return "B"
    if number == 12:
        return "C"
    if number == 13:
        return "D"
    if number == 14:
        return "E"
    if number == 15:
        return "F"

def one_dee_six():
    return random.randint(1,6)

def sum_two_dee_six():
    return one_dee_six() + one_dee_six()

def roll_size():
    size_result = sum_two_dee_six() - 2
    if size_result == 10:
        return "A"
    else:
        return size_result

def roll_atmosphere(planet_size):
    if planet_size == "A":
        planet_size = 10
    unusual_chance = random.randint(0,100)
    
    if (planet_size == 0 or planet_size == 1):
        return 0
    elif (unusual_chance == 0 or unusual_chance == 100):
        return "F"
    else:
        number = (sum_two_dee_six() - 7 + planet_size)
        if number < 0:
            return 0
        elif number > 15:
            return "F"
        elif (number >= 10):
            return numbers_to_letters(number)
        else:
            return number
        

def roll_hydrographics(planet_size, planet_atmosphere):
    if (planet_size == "A"):
        planet_size = 10
    if (planet_atmosphere == "A"):
        planet_atmosphere = 10
    if (planet_atmosphere == "B"):
        planet_atmosphere = 11
    if planet_atmosphere == "C":
        planet_atmosphere = 12
    if planet_atmosphere == "D":
        planet_atmosphere = 13
    if planet_atmosphere == "E":
        planet_atmosphere = 14
    if planet_atmosphere == "F":
        planet_atmosphere = 15

    if (planet_size == 0 or planet_size == 1):
        return 0
    elif (planet_atmosphere == 0 or planet_atmosphere == 1 or planet_atmosphere == 10 or planet_atmosphere == 11 or planet_atmosphere == 12):
        number = sum_two_dee_six() - 11 + planet_atmosphere
        if number < 0:
            return 0
        elif number > 9:
            return "A"
        else:
            return number
    else:
        number = (sum_two_dee_six() - 7 + planet_atmosphere)
        if number < 0:
            return 0
        elif number >= 10:
            return "A"
        else:
            return number

def roll_temperature(planet_atmosphere):
    if (planet_atmosphere == 0 or planet_atmosphere == 1):
        return "Variable"
    elif (planet_atmosphere == 2 or planet_atmosphere == 3):
        return sum_two_dee_six() - 2
    elif (planet_atmosphere == 4 or planet_atmosphere == 5 or planet_atmosphere == "E"):
        return sum_two_dee_six() - 1
    elif (planet_atmosphere == 6 or planet_atmosphere == 7):
        return sum_two_dee_six()
    elif (planet_atmosphere == 8 or planet_atmosphere == 9):
        return sum_two_dee_six() + 1
    elif (planet_atmosphere == "A" or planet_atmosphere == "D" or planet_atmosphere == "F"):
        return sum_two_dee_six() + 2
    else:
        return sum_two_dee_six() + 6

def roll_population(planet_size, planet_atmosphere):
    if (planet_size == 6 or planet_size == 7 or planet_size == 8 or planet_size == 9) and (planet_atmosphere == 6):
        return random.randint(6,7)
    else:
        return random.randint(0,5)

def roll_government(planet_population):
    if (planet_population == 0):
        return 0
    else:
        gov_result = sum_two_dee_six() + planet_population - 4
        if gov_result < 0:
            return 0
        elif (gov_result >= 10):
            return numbers_to_letters(gov_result)
        else:
            return gov_result

def roll_law_level(planet_government):
    if (planet_government == "A"):
        planet_government = 10
    if (planet_government == "B"):
        planet_government = 11
    if planet_government == "C":
        planet_government = 12
    if planet_government == "D":
        planet_government = 13
    if planet_government == "E":
        planet_government = 14
    if planet_government == "F":
        planet_government = 15
    
    if (planet_government == 0):
        return 0
    else:
        law_result = sum_two_dee_six() + planet_government - 7
        if law_result < 0:
            return 0
        elif law_result > 9:
            return 9
        else:
            return law_result

def roll_startport(planet_population):
    if planet_population <= 2:
        return sum_two_dee_six() - 2
    elif (planet_population <= 4 and planet_population > 2):
        return sum_two_dee_six() - 1
    elif (planet_population >= 8 and planet_population < 10):
        return sum_two_dee_six() + 1
    else:
        return sum_two_dee_six()

def starport_calc(planet_population):
    
    result = roll_startport(planet_population)
    if (result <= 2):
        return "X"
    elif (result == 3 or result == 4):
        return "E"
    elif (result == 5 or result == 6):
        return "D"
    elif (result == 7 or result == 8):
        return "C"
    elif (result == 9 or result == 10):
        return "B"
    else:
        return "A"

def roll_tech_level(rolled_population, rolled_atmosphere):
    
    if (rolled_population == 0):
        return 0
    elif (rolled_population < 6):
        result = one_dee_six()
        if (rolled_atmosphere == 0 or rolled_atmosphere == 1):
            return 8
        elif (rolled_atmosphere == 2 or rolled_atmosphere == 3):
            if result > 5:
                return result
            else:
                return 5
        elif (rolled_atmosphere == 4 or rolled_atmosphere == 7 or rolled_atmosphere == 9):
            if (result > 3):
                return result
            else:
                return 3
        elif (rolled_atmosphere == "A"):
            return 8
        elif (rolled_atmosphere == "B"):
            return 9
        elif (rolled_atmosphere == "C"):
            return "A"
        elif (rolled_atmosphere == "D" or rolled_atmosphere == "E"):
            if (result > 5):
                return result
            else:
                return 5
        elif (rolled_atmosphere == "F"):
            return 8
        else:
            return result
    elif (rolled_population == 6 or rolled_population == 7):
        return "A"