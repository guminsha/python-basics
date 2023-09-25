# map() = applies a function to each item in an iterable (list, tuple, etc)

store = [("Shirt", 20.00),
         ("Pants", 25.00),
         ("Jacket", 50.00),
         ("Socks", 10.00)]

to_brl = lambda data: (data[0], round(data[1]*5.65, 2))
to_dollar = lambda data: (data[0], round(data[1]*4.94, 2))

store_brl = list(map(to_brl, store))
store_dollar = list(map(to_dollar, store))

for i in store_brl:
    print(i)

for i in store_dollar:
    print(i)
