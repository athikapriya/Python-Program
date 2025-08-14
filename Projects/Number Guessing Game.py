from random import randint

win = 0
loss = 0

for x in range(1, 6):
    guessNumber = int(input("Enter a number between 1 to 5 : "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("Congratulations! You guessed right")
        win += 1

    else:
        print("Oops! You guessed wrong")
        loss += 1
        print("Random Number : ", randomNumber)

print("You won", win, "times")
print("You loss", loss, "times")

