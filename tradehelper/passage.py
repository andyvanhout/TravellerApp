import traffic

def highpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + amber_modifier + red_modifier - 4 #minus four for high passage
    #print(f'Dice Modifier for High Passage: {dice_modifier}')
    high_passengers = traffic.passenger_traffic(dice_modifier)
    print(f'Number of High Passengers: {high_passengers}')

def mediumpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + amber_modifier + red_modifier
    #print(f'Dice Modifier for Medium Passage: {dice_modifier}')
    medium_passengers = traffic.passenger_traffic(dice_modifier)
    print(f'Number of Medium Passengers: {medium_passengers}')

def basicpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + amber_modifier + red_modifier
    #print(f'Dice Modifier for Basic Passage: {dice_modifier}')
    basic_passengers = traffic.passenger_traffic(dice_modifier)
    print(f'Number of Basic Passengers: {basic_passengers}')

def lowpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + amber_modifier + red_modifier + 1 #plus one for low passage
    #print(f'Dice Modifier for Low Passage: {dice_modifier}')
    low_passengers = traffic.passenger_traffic(dice_modifier)
    print(f'Number of Low Passengers: {low_passengers}')
