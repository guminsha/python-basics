# str.format() = optional method that gives users more control
#                when displaying outputs

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #positional argument
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument
# print("The {1} jumped over the {1}".format(animal, item)) #positional argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Brian"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {name:10}. Nice to meet you".format(name="Rougert"))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))  # Left Alignment (Default)
# print("Hello, my name is {:>10}. Nice to meet you".format(name))  # Right Alignment
# print("Hello, my name is {:^10}. Nice to meet you".format(name))  # Center Alignment

number = 3.141592
number2 = 1000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2))
print("The number pi is {:o}".format(number2))
print("The number pi is {:X}".format(number2))
print("The number pi is {:E}".format(number2))
