# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)
