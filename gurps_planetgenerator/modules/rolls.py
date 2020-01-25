import random

def one_dee_six():
    return random.randint(1,6)

def roll_dee_six(number):
    diceroll = 0
    for i in range(number):
        diceroll += one_dee_six()
    return diceroll

def planet_surface_gravity(density, diameter):
    return round((density * diameter)/7930, 2)

def ice_core_density(modifier):
    density_chart = {
        6: 0.3,
        7: 0.4,
        8: 0.4,
        9: 0.4,
        10: 0.4,
        11: 0.5,
        12: 0.5,
        13: 0.5,
        14: 0.5,
        15: 0.6,
        16: 0.6,
        17: 0.6,
        18: 0.7
    }
    density_result = roll_dee_six(3) + modifier
    if density_result <= 6:
        return density_chart[6]
    elif density_result >= 18:
        return density_chart[18]
    else:
        return density_chart[density_result]

def small_iron_core_density(modifier):
    density_chart = {
        6: 0.6,
        7: 0.7,
        8: 0.7,
        9: 0.7,
        10: 0.7,
        11: 0.8,
        12: 0.8,
        13: 0.8,
        14: 0.8,
        15: 0.9,
        16: 0.9,
        17: 0.9,
        18: 1.0
        }
    density_result = roll_dee_six(3) + modifier
    if density_result <= 6:
        return density_chart[6]
    elif density_result >= 18:
        return density_chart[18]
    else:
        return density_chart[density_result]

def large_iron_core_density(modifier):
    density_chart = {
        6: 0.8,
        7: 0.9,
        8: 0.9,
        9: 0.9,
        10: 0.9,
        11: 1.0,
        12: 1.0,
        13: 1.0,
        14: 1.0,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.2,
        20: 1.2,
        21: 1.3,
        22: 1.3,
        23: 1.3,
        24: 1.4
        }
    density_result = roll_dee_six(3) + modifier
    if density_result <= 6:
        return density_chart[6]
    elif density_result >= 18:
        return density_chart[18]
    else:
        return density_chart[density_result]

def roll_type():
    type_result = roll_dee_six(4)
    if type_result <= 7:
        return ["Asteroid Belt", "-"]
    elif (type_result == 8 or type_result == 9):
        barren_result = roll_dee_six(3)
        if barren_result <= 12:
            return ["Barren (Rock)", "-"]
        else:
            return ["Barren (Ice)", "-"]
    elif type_result == 10:
        return ["Desert (Rock)", ""]
    elif (type_result == 11 or type_result == 12):
        return ["Garden", "Very Thin"]
    elif (type_result == 13 or type_result == 14):
        return ["Garden", "Thin"]
    elif (type_result == 15 or type_result == 16):
        return ["Garden", "Standard"]
    elif (type_result == 17 or type_result == 18):
        return ["Garden", "Dense"]
    elif (type_result >= 19 and type_result <= 21):
        hostile_result = roll_dee_six(3)
        if (hostile_result == 3 or hostile_result == 4):
            return ["Subgiant", ""]
        elif (hostile_result == 5 or hostile_result == 6):
            return ["Desert (Ice)", ""]
        elif (hostile_result >= 7 and hostile_result <= 9):
            return ["Glacier", ""]
        elif (hostile_result >= 10 and hostile_result <= 15):
            return ["Pre-Garden", ""]
        else:
            return ["Greenhouse", ""]
    else:
        return ["Garden", "Very Dense"]

def roll_size(planet_type, planet_atmosphere):
    if planet_type == "Asteroid Belt":
        return ["None", "None", "None"]

    elif planet_type == "Barren (Ice)":
        size_result = roll_dee_six(3)
        if size_result <= 8:
            diameter = 1000
            density = ice_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 9 and size_result <= 12):
            diameter = 1500
            density = ice_core_density(-1)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 2000
            density = ice_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 2500
            density = ice_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 3000
            density = ice_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif planet_type == "Barren (Rock)":
        size_result = roll_dee_six(3)
        if size_result <= 8:
            diameter = 1000
            density = small_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 9 and size_result <= 10):
            diameter = 1500
            density = small_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 11 or size_result == 12):
            diameter = 2000
            density = small_iron_core_density(-1)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 2500
            density = small_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 2500
            density = small_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 17):
            diameter = 3500
            density = small_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 4000
            density = small_iron_core_density(-12)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif planet_type == "Desert (Ice)":
        size_result = roll_dee_six(3)
        if size_result <= 8:
            diameter = 3000
            density = ice_core_density(8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 9 and size_result <= 12):
            diameter = 3500
            density = ice_core_density(4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 4000
            density = ice_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 5500
            density = ice_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 6000
            density = ice_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif planet_type == "Desert (Rock)":
        size_result = roll_dee_six(3)
        if size_result <= 5:
            diameter = 3000
            density = ice_core_density(12)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 6 and size_result <= 8):
            diameter = 3500
            density = small_iron_core_density(4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 9 and size_result <= 12):
            diameter = 4000
            density = small_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 13 and size_result <= 15):
            diameter = 4500
            density = small_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 5000
            density = small_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif (planet_type == "Garden" or planet_type == "Pre-Garden"):
        if (planet_type == "Garden" and planet_atmosphere == "Very Thin"):
            size_result = roll_dee_six(3) - 6
        elif (planet_type == "Garden" and planet_atmosphere == "Thin"):
            size_result = roll_dee_six(3) - 3
        elif (planet_type == "Garden" and planet_atmosphere == "Dense"):
            size_result = roll_dee_six(3) + 3
        elif (planet_type == "Garden" and planet_atmosphere == "Very Dense"):
            size_result = roll_dee_six(3) + 6
        else:
            size_result = roll_dee_six(3)

        if size_result <= 3:
            diameter = 4500
            density = large_iron_core_density(15)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 4):
            diameter = 5000
            density = large_iron_core_density(8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 5 or size_result == 6):
            diameter = 5500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 7 or size_result == 8):
            diameter = 6000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 9 or size_result == 10):
            diameter = 6500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 11 or size_result == 12):
            diameter = 7000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 7500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 8000
            density = large_iron_core_density(-1)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 17):
            diameter = 8500
            density = large_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 9000
            density = large_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
    
    elif (planet_type == "Glacier"):
        size_result = roll_dee_six(3)
        if size_result <= 3:
            diameter = 4000
            density = large_iron_core_density(12)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 4):
            diameter = 4500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 5 or size_result == 6):
            diameter = 5000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 7 or size_result == 8):
            diameter = 5500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 9 or size_result == 10):
            diameter = 6000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 11 or size_result == 12):
            diameter = 6500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 7000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 7500
            density = large_iron_core_density(-1)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 17):
            diameter = 8000
            density = large_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 8500
            density = large_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif (planet_type == "Greenhouse"):
        size_result = roll_dee_six(3)
        if size_result <= 3:
            diameter = 4500
            density = large_iron_core_density(15)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 4):
            diameter = 5000
            density = large_iron_core_density(8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 5):
            diameter = 5500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 6):
            diameter = 6000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 7 or size_result == 8):
            diameter = 6500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 9 or size_result == 10):
            diameter = 7000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 11 or size_result == 12):
            diameter = 7500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 13 or size_result == 14):
            diameter = 8000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 15 or size_result == 16):
            diameter = 8500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 16):
            diameter = 9000
            density = large_iron_core_density(-1)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result == 17):
            diameter = 9500
            density = large_iron_core_density(-4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 10000
            density = large_iron_core_density(-8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

    elif (planet_type == "Subgiant"):
        size_result = roll_dee_six(3)
        if size_result <= 4:
            diameter = 8000
            density = large_iron_core_density(8)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 5 and size_result <= 7):
            diameter = 8500
            density = large_iron_core_density(4)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 8 and size_result <= 10):
            diameter = 9000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        elif (size_result >= 11 and size_result <= 13):
            diameter = 9500
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]
        else:
            diameter = 10000
            density = large_iron_core_density(0)
            gravity = planet_surface_gravity(density, diameter)
            return [diameter, density, gravity]

def atmosphere_type(planet_type):
    if (planet_type == "Asteroid Belt" or planet_type == 'Barren (Ice)' or planet_type == 'Barren (Rock)'):
        return "None (vacuum)."
    elif (planet_type == "Desert (Ice)"):
        result = roll_dee_six(3)
        if result <= 9:
            return "Toxic"
        else:
            return "Corrosive"
    elif (planet_type == "Desert (Rock)"):
        result = roll_dee_six(3)
        if result <= 15:
            return "Trace"
        else:
            return "Very thin"
    elif (planet_type == "Glacier" or planet_type == "Pre-Garden"):
        result = roll_dee_six(3)
        if result <= 12:
            return "Suffocating"
        else:
            return "Toxic"
    elif (planet_type == "Greenhouse"):
        result = roll_dee_six(3)
        if result <= 12:
            return "Suffocating"
        else:
            return "Toxic"
    elif (planet_type == Subgiant):
        result = roll_dee_six(3)
        if result <= 12:
            Insidious
        else:
            return "Corrosive"