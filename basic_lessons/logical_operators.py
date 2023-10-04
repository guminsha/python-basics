# logical operators (and, or, not) = used to check if two or more statements are true

temp = int(input("What's the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today, enjoy!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today, stay inside!")

