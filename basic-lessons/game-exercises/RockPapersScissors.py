import random

player_points = 0
computer_points = 0

while True:
    choices = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Chose Rock, Paper or Scissors: ").lower()

    print("Player choice: {}".format(player))
    print("Computer choice: {1}".format(player, computer))

    if player == computer:
        print("Its a tie!")

    elif player == "rock":
        if computer == "scissors":
            print("You Won!")
            player_points += 1
        else:
            print("You Lose!")
            computer_points += 1

    elif player == "paper":
        if computer == "rock":
            print("You Won!")
            player_points += 1
        else:
            print("You Lose!")
            computer_points += 1

    elif player == "scissors":
        if computer == "paper":
            print("You Won!")
            player_points += 1
        else:
            print("You Lose!")
            computer_points += 1

    print("Scoreboard:\nPlayer's Score: {0}\nComputer's Score: {1}".format(player_points, computer_points))
    play_again = input("Do you want to play again? (yes or no): ").lower()

    if play_again == "no":
        break

print("Game Over")
