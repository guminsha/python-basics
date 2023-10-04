# scope = it's the region where the variable is recognized
#         A variable is only available from inside the region it's created
#         A global and locally scoped versions of a variable can be created

name = "Rougert"  # global scope (available inside and outside of functions)


def display_name():
    name = "Brian"  # local scope (available only inside this function)
    print(name)


display_name()
print(name)
