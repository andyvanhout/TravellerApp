import rolls

class TravellerPlanet(object):
    def __init__(self, size, atmosphere, hydrographics, temperature, population):
        self.size = size
        self.atmosphere = atmosphere
        self.hydrographics = hydrographics
        self.temperature = temperature
        self.population = population

def roll_planet():
    rolled_size = rolls.roll_size()
    rolled_atmosphere = rolls.roll_atmosphere(rolled_size)
    rolled_hydrographics = rolls.roll_hydrographics(rolled_size, rolled_atmosphere)
    rolled_temperature = rolls.roll_temperature(rolled_atmosphere)
    rolled_population = rolls.roll_population(rolled_size, rolled_atmosphere)
    results = {"size": rolled_size, "atmosphere": rolled_atmosphere, "hydrographics": rolled_hydrographics,
               "temperature": rolled_temperature, "population": rolled_population}
    return results

rr = roll_planet()

newplanet = TravellerPlanet(rr['size'], rr['atmosphere'], rr['hydrographics'], rr['temperature'], rr['population'])
print(f'Size: {newplanet.size}, Atmosphere: {newplanet.atmosphere}, Hydrographics: {newplanet.hydrographics}, Temperature: {newplanet.temperature}, Population {newplanet.population}')