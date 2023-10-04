# filter() = creates a collection of elements from a an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Evandro", 27),
           ("Leonardo", 18),
           ("Caio", 25),
           ("Victor", 16),
           ("Luan", 30),
           ("Brian", 17)]

# name = lambda data: data[0]   friends.sort(key=name)

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
