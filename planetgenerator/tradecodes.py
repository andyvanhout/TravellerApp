def calculate_trade_codes(size, atmosphere, hydro, population, government, law_level, tech_level):
    trade_codes = []
    if (atmosphere >= 4 and atmosphere <= 9) and (hydro >= 4 and hydro <= 8) and (population >= 5 and population <= 7):
        trade_codes.append("Ag")
    if (size == 0 and atmosphere == 0 and hydro == 0):
        trade_codes.append("As")
    if (population == 0 and government == 0 and law_level == 0):
        trade_codes.append("Ba")
    if (atmosphere >= 2) and (hydro == 0):
        trade_codes.append("De")
    if (atmosphere >= 10) and (hydro >= 1):
        trade_codes.append("Fl")
    if (size >= 6 and size <= 8) and (atmosphere == 5 or atmosphere == 6 or atmosphere == 8) and (hydro >= 5 and hydro <= 7):
        trade_codes.append("Ga")
    if (population >= 8):
        trade_codes.append("Hi")
    if (tech_level >= 11):
        trade_codes.append("Ht")
    if (atmosphere == 0 or atmosphere == 1) and (hydro >= 1):
        trade_codes.append("Ie")
    if (atmosphere >= 0 and atmosphere <= 2 or atmosphere == 4 or atmosphere == 7 or atmosphere == 9) and (population >= 7):
        trade_codes.append("In")
    if (population > 0 and population <= 3):
        trade_codes.append("Lo")
    if (tech_level <= 4 and tech_level > 0):
        trade_codes.append("Lt")
    if (atmosphere >= 0 and atmosphere <= 3) and (hydro >= 0 and hydro <= 3) and (population >= 5):
        trade_codes.append("Na")
    if (population > 0 and population < 5):
        trade_codes.append("Ni")
    if (atmosphere >= 2 and atmosphere <= 5) and (hydro >= 0 and hydro <= 3):
        trade_codes.append("Po")
    if (atmosphere == 6 or atmosphere == 8) and (population >= 6) and (government >= 4 and government <= 9):
        trade_codes.append("Ri")
    if (atmosphere == 0):
        trade_codes.append("Va")
    if (hydro >= 10):
        trade_codes.append("Wa")
    return trade_codes
