from random import *

solution = int(randrange(1,11))

def game():
    print("Guess a number between 1 and 10")
    while solution == None:
        userguess = int(input("Enter your guess!: "))
        if solution == userguess:
            print("You guessed the right answer which was " +str(solution))
            break
        else:
            print("You guessed the wrong solution :(")
            print("Try again!")
            pass
game()
