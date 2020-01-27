import random

import modules.rolls as rolls

def roll_planet():
    rolled_planet_type = rolls.planet_type()
    rolled_size = rolls.size(rolled_planet_type['type'], rolled_planet_type['atmosphere'])
    rolled_atmosphere = rolls.atmosphere_type(rolled_planet_type['type'])
    if rolled_planet_type['atmosphere'] == '':
        rolled_planet_type['atmosphere'] = rolled_atmosphere
    elif rolled_atmosphere == '':
        pass
    else:
        rolled_planet_type['atmosphere'] += ' ' + rolled_atmosphere
    rolled_hydrosphere = rolls.hydrographics(rolled_planet_type['type'])

    combined_properties = {**rolled_planet_type, **rolled_size, **rolled_hydrosphere}
    with open("output.txt", "a") as text_file:
        print(combined_properties, file=text_file)
    print(combined_properties)

for x in range(500):
    roll_planet()
