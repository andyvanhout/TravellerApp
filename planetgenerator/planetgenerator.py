import rolls

class travellerplanet(object):

    rolled_size = rolls.roll_size()
    rolled_atmosphere = rolls.roll_atmosphere(rolled_size)
    rolled_hydrographics = rolls.roll_hydrographics(rolled_size, rolled_atmosphere)
    rolled_temperature = rolls.roll_temperature(rolled_atmosphere)

    planetproperties = {
        'size': rolled_size,
        'atmosphere': rolled_atmosphere,
        'hydrographics': rolled_hydrographics,
        'temperature': rolled_temperature
    }

print(travellerplanet.planetproperties)