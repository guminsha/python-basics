# slicing = creating a substring from another string extracting elements from it
#           indexing[] or slice()
#           [start:stop:step]

name = "Rougert Brian"
first_name = name[:7]      # [0:7]
last_name = name[8:]       # [8:end]
funky_name = name[::2]     # [0:end:2]
reversed_name = name[::-1] # [0:end:-1]

print(first_name)
print(last_name)
print(funky_name)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)

print(website[slice])
print(website2[slice])