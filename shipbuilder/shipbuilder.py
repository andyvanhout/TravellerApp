tons = input("Tonnage>")

def ship_hull_cost(tons):
    return 50000 * int(tons)

def calculate_hull_points(tons):
    tons = int(tons)
    if (tons > 25000 and tons <= 100000):
        return tons / 2
    elif (tons > 100000):
        return tons / 1.5
    else:
        return tons / 2.5

hull_cost = ship_hull_cost(tons)
hull_points = calculate_hull_points(tons)
print(hull_cost)
print(hull_points)