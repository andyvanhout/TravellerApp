import modules.passage as passage
import random as random

def broker_effect():
    print("Input total DM for broker (Skill and characteristic DM)")
    broker_modifier = int(input(">"))
    broker_roll = random.randint(1, 6) + random.randint(1, 6) + broker_modifier
    broker_target = 8
    
    if broker_roll >= broker_target:
        broker_effect = broker_roll - broker_target
    else:
        broker_effect = (broker_target - broker_roll) * -1
    print(f'Broker Effect is {broker_effect}')
    print("--")
    return broker_effect

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

broker_effect = broker_effect()
steward_modifier = steward_skill()
population_modifier_origin = world_population()
population_modifier_destination = world_population()
starport_modifier_origin = starport()
starport_modifier_destination = starport()
amber_modifier_origin = amber_zone()
amber_modifier_destination = amber_zone()
red_modifier_origin = red_zone()
red_modifier_destination = red_zone()

passage.highpassage(broker_effect, steward_modifier, population_modifier_origin, starport_modifier_origin, amber_modifier_origin, red_modifier_origin, population_modifier_destination, starport_modifier_destination, amber_modifier_destination, red_modifier_destination)
passage.mediumpassage(broker_effect, steward_modifier, population_modifier_origin, starport_modifier_origin, amber_modifier_origin, red_modifier_origin, population_modifier_destination, starport_modifier_destination, amber_modifier_destination, red_modifier_destination)
passage.basicpassage(broker_effect, steward_modifier, population_modifier_origin, starport_modifier_origin, amber_modifier_origin, red_modifier_origin, population_modifier_destination, starport_modifier_destination, amber_modifier_destination, red_modifier_destination)
passage.lowpassage(broker_effect, steward_modifier, population_modifier_origin, starport_modifier_origin, amber_modifier_origin, red_modifier_origin, population_modifier_destination, starport_modifier_destination, amber_modifier_destination, red_modifier_destination)