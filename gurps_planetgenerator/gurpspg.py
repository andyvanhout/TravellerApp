import random

import modules.rolls as rolls


""" class TravellerPlanet(object):
    def __init__(self, starport, planet_type, size, density, gravity, atmosphere, hydrographics, climate,
     population, government, law_level, tech_level):
        self.starport = starport
        self.type = planet_type
        self.size = size
        self.density = density
        self.gravity = gravity
        self.atmosphere = atmosphere
        self.hydrographics = hydrographics
        self.climate = climate
        self.population = population
        self.government = government
        self.law_level = law_level
        self.tech_level = tech_level """

def roll_planet():
    rolled_planet_type = rolls.roll_type()
    rolled_size = rolls.roll_size(rolled_planet_type[0], rolled_planet_type[1])
    printout = rolled_planet_type + rolled_size

    with open("output.txt", "a") as text_file:
        print(printout, file=text_file)
    print(printout)

for x in range(50):
    roll_planet()
