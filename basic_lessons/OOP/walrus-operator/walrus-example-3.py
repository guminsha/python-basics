my_numbers = [5, 7, 18, 28, 8, 2, 3, 109, 4]


def process_number(n):
    return  n ** 2 + 5


# myresults = [process_number(x) for x in mynumbers if process_number(x) < 100]
my_results = [result for x in my_numbers if (result := process_number(x)) < 100]

print(my_results)
