import modules.cargo as cargo

def skill_effect():
    print("Input the effect of Streetwise or Steward Check")
    skill_effect = int(input(">"))
    print(f'Effect is {skill_effect}')
    print("--")
    return skill_effect

def world_population():
    print("Input world population")
    world_population = int(input(">"))
    print(f'World population is {world_population}')
    print("--")

    if (world_population <= 1):
        return -4
    elif (world_population == 6 or world_population == 7):
        return 2
    elif (world_population >= 8):
        return 4
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

def tech_level():
    print("Input Tech Level")
    tech_level = int(input(">"))
    print(f'Planet Tech Level is: {tech_level}')
    print("--")

    if (tech_level <= 6):
        return -1
    elif (tech_level >= 9):
        return 2
    else:
        return 0

def amber_zone():
    print("Amber zone? 1 is yes, 0 is no")
    amber_zone = int(input(">"))
    print(f'Amber Zone: {amber_zone}')

    if (amber_zone == 1):
        return -2
    else:
        return 0

def red_zone():
    print("Red zone? 1 is yes, 0 is no")
    red_zone = int(input(">"))
    print(f'Red Zone: {red_zone}')

    if (red_zone == 1):
        return -6
    else:
        return 0

skill_effect = skill_effect()
population_modifier = world_population()
starport_modifier = starport()
tech_level = tech_level()
amber_modifier = amber_zone()
red_modifier = red_zone()

cargo.major_cargo(skill_effect, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier)
cargo.minor_cargo(skill_effect, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier)
cargo.incidental_cargo(skill_effect, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier)
