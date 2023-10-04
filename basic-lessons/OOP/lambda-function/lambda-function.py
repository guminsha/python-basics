# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (thinks of it as a shortcut) (usefull if needed for a short period of time, throw-away)
# lambda parameters:expression

# def double(x):
#    return x * 2

# print(double(5))

double = lambda x: x * 2
print(double(5))

multiply = lambda x, y: x * y
print(multiply(5, 25))

add = lambda x, y, z: x + y + z
print(add(10, 30, 50))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Rougert Brian", "Alexandre"))

age_check = lambda age: True if age >= 18 else False
print(age_check(17))
