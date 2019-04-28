import traffic

def major_cargo(steward_skill, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + tech_level + amber_modifier + red_modifier - 4 #minus four for major cargo
    #print(f'Dice Modifier for High Passage: {dice_modifier}')
    major_lots = traffic.freight_traffic(dice_modifier)
    print(f'Number of Major Lots: {major_lots}')

def minor_cargo(steward_skill, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + tech_level + amber_modifier + red_modifier
    #print(f'Dice Modifier for Medium Passage: {dice_modifier}')
    minor_lots = traffic.freight_traffic(dice_modifier)
    print(f'Number of Minor Lots: {minor_lots}')

def incidental_cargo(steward_skill, population_modifier, starport_modifier, tech_level, amber_modifier, red_modifier):
    dice_modifier = steward_skill + population_modifier + starport_modifier + tech_level + amber_modifier + red_modifier + 2 #plus two for incidental cargo
    #print(f'Dice Modifier for Basic Passage: {dice_modifier}')
    incidental_lots = traffic.freight_traffic(dice_modifier)
    print(f'Number of Incidental Lots: {incidental_lots}')