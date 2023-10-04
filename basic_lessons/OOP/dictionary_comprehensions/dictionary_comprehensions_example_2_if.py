# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable

weather = {"New York": "Snowing", "Boston": "Sunny", "Los Angeles": "Sunny", "Chicago": "Cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "Sunny"}

print(sunny_weather)