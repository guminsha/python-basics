#done = False
#while not done:
#    command = input("Please enter a command ('q' = quit): ")
#    if command == "q":
#        done = True
#    else:
#        print(f"Your command was {command}")

# -----------------------------------

while (command := input("Please enter a command ('q' = quit): ")) != "q":
    print(f"Your command was {command}")
