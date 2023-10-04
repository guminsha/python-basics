# foods = list()

# while True:
#    food = input("What food do you like? ")
#    if food == "quit":
#        break
#    foods.append(food)

# print(foods)

# -----------------------------------
foods = list()
food = ""

while (food := input("What food do you like? ")) != "quit":
    foods.append(food)

print(foods)
