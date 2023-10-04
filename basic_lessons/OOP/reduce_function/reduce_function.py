# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)

import functools

# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y: x+y, letters) # x = first elements, y = second element (H, E) then (HE, L)... until HELLO
# print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)  # this time we multiply the elements
print(result)
