# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a variaty amount of arguments

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3, 5, 11))
