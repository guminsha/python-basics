# Higher order function = a function that either:
#                         1. Accepts function as argument
#                         or
#                         2. Returns a function
#                         (In Python, functions are also treated as objects)

def divisor(x):
    def dividend(y):
        return y / x

    return dividend  # returns the memory address of dividend


divide = divisor(2)
divide2 = divisor(4)

print(divide(10))
print(divide2(40))
# print(divisor(2)(10))
# print(divisor(4)(40)
