from random import randint

def guess():
    print("Welcome to guess the number!\n " + 
        "This is a game where I think of a random number between 1 - 100 and you " +
        "try to guess what it is.\n If your guess is higher than my number, I will " +
        "say 'Too High', if it's lower, I will say 'Too Low'.\n Let's begin!")
    randNumber = randint(1, 100)
    guessedCorrectly = False
    while (guessedCorrectly == False):
        userGuess = input ("Please guess a number ")
        try:
            guess = int(userGuess)
            if guess > randNumber:
                print("Too High")
            elif guess < randNumber:
                print("Too Low")
            else:
                print("Correct! The number was",randNumber,"!\n")
                guessedCorrectly = True

        except ValueError:
                print("That is not a valid number")


guess()
