# 2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburguer", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

#print(food)

for i in food:
    for j in i:
        print(j)
