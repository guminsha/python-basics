# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true

name = ""
#name = None

#while not name:
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)