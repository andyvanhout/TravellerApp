import passage

def steward_skill():
    print("Input highest Steward skill on ship")
    steward_skill = int(input(">"))
    print(f'Steward Skill is {steward_skill}')
    print("--")
    return steward_skill

def world_population():
    print("Input world population")
    world_population = int(input(">"))
    print(f'World population is {world_population}')
    print("--")

    if (world_population <= 1):
        return -4
    elif (world_population == 6 or world_population == 7):
        return 1
    elif (world_population >= 8):
        return 3
    else:
        return 0

def starport():
    print("Input starport class")
    starport = input(">").upper()
    print(f'Starport Class is: {starport}')
    print("--")

    if (starport == 'A'):
        return 2
    elif (starport == 'B'):
        return 1
    elif (starport == 'E'):
        return -1
    elif (starport == 'X'):
        return -3
    else:
        return 0

def amber_zone():
    print("Amber zone? 1 is yes, 0 is no")
    amber_zone = int(input(">"))
    print(f'Amber Zone: {amber_zone}')

    if (amber_zone == 1):
        return 1
    else:
        return 0

def red_zone():
    print("Red zone? 1 is yes, 0 is no")
    red_zone = int(input(">"))
    print(f'Red Zone: {red_zone}')

    if (red_zone == 1):
        return -4
    else:
        return 0

steward_skill = steward_skill()
population_modifier = world_population()
starport_modifier = starport()
amber_modifier = amber_zone()
red_modifier = red_zone()

passage.highpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier)
passage.mediumpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier)
passage.basicpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier)
passage.lowpassage(steward_skill, population_modifier, starport_modifier, amber_modifier, red_modifier)