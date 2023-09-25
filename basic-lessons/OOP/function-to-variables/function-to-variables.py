def hello():
    print("Hello")

print(hello) # memory adress
hi = hello
print(hi) # same hello's adress

print("hi adress: "+str(hi)+"\nhello adress: "+str(hello))

hi()
hello()

say = print
say("Whoa: I cant believe this works: :0")


