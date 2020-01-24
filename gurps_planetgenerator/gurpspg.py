import random



class TravellerPlanet(object):
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
        self.tech_level = tech_level

def roll_planet():
    rolled_planet_type
    rolled_size = rolls.roll_size()
    rolled_density
    rolled_gravity
    rolled_atmosphere = rolls.roll_atmosphere(rolled_size)
    rolled_hydrographics = rolls.roll_hydrographics(rolled_size, rolled_atmosphere)
    rolled_climate
    rolled_population = rolls.roll_population(rolled_size, rolled_atmosphere)
    rolled_government = rolls.roll_government(rolled_population)
    rolled_law_level = rolls.roll_law_level(rolled_government)
    rolled_starport = rolls.starport_calc(rolled_population)
    rolled_tech_level = rolls.roll_tech_level(rolled_population, rolled_atmosphere)
    rolled_temperature = rolls.roll_temperature(rolled_atmosphere)

    results = {"starport": rolled_starport, "size": rolled_size, "atmosphere": rolled_atmosphere, "hydrographics": rolled_hydrographics,
               "temperature": rolled_temperature, "population": rolled_population, "government": rolled_government,
               "law_level": rolled_law_level, "tech_level": rolled_tech_level
               }
    
    return results

def print_new_planets():
    
    rr = roll_planet()

    newplanet = TravellerPlanet(rr['starport'], rr['size'], rr['atmosphere'], rr['hydrographics'], rr['population'],
    rr['government'], rr['law_level'], rr['tech_level'])

    converted_size = rolls.letters_to_numbers(newplanet.size)
    converted_atmosphere = rolls.letters_to_numbers(newplanet.atmosphere)
    converted_hydrographics = rolls.letters_to_numbers(newplanet.hydrographics)
    converted_population = rolls.letters_to_numbers(newplanet.population)
    converted_government = rolls.letters_to_numbers(newplanet.government)
    converted_law_level = rolls.letters_to_numbers(newplanet.law_level)
    converted_tech_level = rolls.letters_to_numbers(newplanet.tech_level)

    planet_trade_list = tradecodes.calculate_trade_codes(converted_size, converted_atmosphere, converted_hydrographics,
    converted_population, converted_government, converted_law_level, converted_tech_level)

    planet_trade_codes = " ".join(planet_trade_list)
    printout = f"""{newplanet.starport}{newplanet.size}{newplanet.atmosphere}{newplanet.hydrographics}\
{newplanet.population}{newplanet.government}{newplanet.law_level}-{newplanet.tech_level} """ + "| " + planet_trade_codes
    
    with open("output.txt", "a") as text_file:
        print(printout, file=text_file)
    print(printout)

for x in range(114):
    print_new_planets()

