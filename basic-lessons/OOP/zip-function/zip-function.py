# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("password", "abc123", "guest")
login_date = ["07/01/2023", "11/01/2023", "23/01/2023"]

# logins = list(zip(usernames, passwords))
logins = dict(zip(login_date, zip(usernames, passwords)))  # created a dictionary using login_date as key
#                                                             (I need to search more about it)
for key, value in logins.items():
    print(key, value)

# print(type(logins))

logins = zip(usernames, passwords, login_date)

for i in logins:
    print(i)
