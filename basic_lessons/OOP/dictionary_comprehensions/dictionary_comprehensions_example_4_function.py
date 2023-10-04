# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 40 <= value <= 69:
        return "WARM"
    else:
        return "COLD"


cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}

print(desc_cities)
