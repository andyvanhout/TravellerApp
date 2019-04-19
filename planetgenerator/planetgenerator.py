import rolls

# rolled_temperature = rolls.roll_temperature(rolled_atmosphere)

class TravellerPlanet(object):
    def __init__(self, size, atmosphere, hydrographics, population, government, law_level, tech_level, starport):
        self.size = size
        self.atmosphere = atmosphere
        self.hydrographics = hydrographics
        self.population = population
        self.government = government
        self.law_level = law_level
        self.tech_level = tech_level
        self.starport = starport

def roll_planet():
    rolled_size = rolls.roll_size()
    rolled_atmosphere = rolls.roll_atmosphere(rolled_size)
    rolled_hydrographics = rolls.roll_hydrographics(rolled_size, rolled_atmosphere)
    rolled_population = rolls.roll_population(rolled_size, rolled_atmosphere)
    rolled_government = rolls.roll_government(rolled_population)
    rolled_law_level = rolls.roll_law_level(rolled_government)
    rolled_starport = rolls.starport_calc(rolled_population)
    rolled_tech_level = rolls.roll_tech_level(rolled_population, rolled_atmosphere)
    rolled_temperature = rolls.roll_temperature(rolled_atmosphere)

    results = {"size": rolled_size, "atmosphere": rolled_atmosphere, "hydrographics": rolled_hydrographics,
               "temperature": rolled_temperature, "population": rolled_population, "government": rolled_government,
               "law_level": rolled_law_level, "starport": rolled_starport, "tech_level": rolled_tech_level
               }
    
    return results

def print_new_planets():
    
    rr = roll_planet()

    newplanet = TravellerPlanet(rr['size'], rr['atmosphere'], rr['hydrographics'], rr['population'],
    rr['government'], rr['law_level'], rr['tech_level'], rr['starport'] )

    printout = f"{newplanet.size}{newplanet.atmosphere}{newplanet.hydrographics}{newplanet.population}{newplanet.government}{newplanet.law_level}{newplanet.starport}-{newplanet.tech_level}"
    print (printout)


for x in range (500):
    print_new_planets()

