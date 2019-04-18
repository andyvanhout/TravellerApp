import rolls

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
    rolled_temperature = rolls.roll_temperature(rolled_atmosphere)
    rolled_population = rolls.roll_population(rolled_size, rolled_atmosphere)
    rolled_government = rolls.roll_government(rolled_population)
    rolled_law_level = 3
    rolled_tech_level = 9
    rolled_starport = "A"
    
    results = {"size": rolled_size, "atmosphere": rolled_atmosphere, "hydrographics": rolled_hydrographics,
               "temperature": rolled_temperature, "population": rolled_population, "government": rolled_government,
               "law_level": rolled_law_level, "tech_level": rolled_tech_level, "starport": rolled_starport
               }
    
    return results

rr = roll_planet()

newplanet = TravellerPlanet(rr['size'], rr['atmosphere'], rr['hydrographics'], rr['temperature'], rr['population'],
rr['government'], rr['law_level', rr['tech_level'], rr['starport'] )
printout = f"""
Size: {newplanet.size}, Atmosphere: {newplanet.atmosphere}, Hydrographics: {newplanet.hydrographics}, Temperature: {newplanet.temperature}, 
Population {newplanet.population}, Government {newplanet.government}, Law Level {newplanet.law_level}, Tech Level: {newplanet.tech_level}
Starport Class: {newplanet.starport}
"""

print(printout)