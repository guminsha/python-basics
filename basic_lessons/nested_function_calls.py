# nested function calls = function calls inside other function
#   the innermost function are resolved first and returns it values as argument to the next other function

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)

print(round(abs(float((input("Enter a whole positive number: "))))))
