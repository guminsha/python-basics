# sort() method = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

grade = lambda grades: grades[1]
age = lambda ages: ages[2]
# students.sort(key=age, reverse=True)  # for lists

sorted_students = sorted(students, key=age)  # for tuples

for i in sorted_students:
    print(i)
