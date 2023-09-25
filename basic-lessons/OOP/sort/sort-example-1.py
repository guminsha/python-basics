# sort() method = used with lists
# sort() function = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

# students.sort(reverse=True) # reverse = True means alphabetically reversed
sorted_student = sorted(students, reverse=True)

for i in sorted_student:
    print(i)
