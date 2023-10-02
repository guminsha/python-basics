def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [21309, 29032, 49382, 8213099, 34980, 493231, 93401, 32920, 394025, 29037]
y = list(map(make_even, x))
print(y)

# y = [make_even(num) for num in x] # list comprehension version
