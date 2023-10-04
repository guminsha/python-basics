def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 0

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[questions_num]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_awser(questions.get(key), guess)
        questions_num += 1
    display_score(correct_guesses, guesses)


def check_awser(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("-----------RESULTS-------------")

    print("Anwsers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")

    print("\nGuesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

    play_again()


def play_again():
    response = input("Do you want to play again? (Y/N): ").upper()
    if response == "Y":
        new_game()
    elif response == "N":
        print("GAME OVER")
        quit()
    else:
        play_again()


questions = {
    "1. Who created Python? ": "A",
    "2. What year was Python created?": "B",
    "3. Python is tributed to which comedy group?": "C",
    "4. Is the Earth round? ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()
