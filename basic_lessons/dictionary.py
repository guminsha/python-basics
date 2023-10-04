# dictionary = A changeable, unordered colletion of unique key:value pairs fast because
#              they use hashing allow us to acess a value quickly

capitals = {'USA': 'Washington DC',
            'Brazil': 'Brasilia',
            'India': 'New Dahli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)

# for i in capitals:
#    print(i)
