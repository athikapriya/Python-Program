from random import choice

choices = ["Rock", "Paper", "Scissors"]
won = 0
loss = 0
tie = 0

for x in range(1, 6):
    player = input("Player chooses [Rock, Paper, Scissors]: ").capitalize()
    computer = choice(choices)

    print("Computer chose : ", computer)

    if computer == player:
        print("It's a tie!")
        tie += 1
    else:
        if player == "Rock":
            if computer == "Scissors":
                print("Player won! Rock crushes Scissors.")
                won += 1
            else:
                print("Computer won! Paper covers Rock.")
                loss += 1
        elif player == "Scissors":
            if computer == "Paper":
                print("Player Won! Scissors crushes Paper.")
                won += 1
            else:
                print("Computer Won! Rock crushes Scissors.")
                loss += 1
        elif player == "Paper":
            if computer == "Rock":
                print("Player Won! Paper crushes Rock.")
                won += 1
            else:
                print("Computer Won! Scissors covers Rock")
                loss += 1
        else:
            print("Invalid choice")

print("Tie", tie, "times")
print("You have won", won, "times")
print("You lost", loss, "times")