# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}

print(desc_cities)