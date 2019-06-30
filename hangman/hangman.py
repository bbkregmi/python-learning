from __future__ import print_function
from random import randint

randomshades = [
        "You are a few hundred years too young to take on this challenge",
        "You lost! But don't feel bad. There are many people who have no talent",
        "Sorry you lost. Maybe you should take a break. You might sprain your brain if you think too much",
        "You have been hanged. Are you always this bad or is today a special occasion?",
        "You lost. I even gave you one of the easier ones. It seems I have underestimated your lack of intelligence",
        "Congratulations! If being hanged was your goal, you have most undeinably attained it!",
        "After some calculations, I have concluded that you are exceptionally poor at this game"
        ]

def findArr(string, character):
    return [i for i, letter in enumerate(string) if letter == character]
def getrandomword():
    filepointer = open("wordlist.txt")
    lines = filepointer.readlines()
    randomword = lines[randint(0, len(lines))].lower()
    return randomword[:-1]

def playhangman(randomword):
    tries_left = 5
    guessed_letters = []
    player_has_won = False

    # Contains current state of game. Unguessed letters are indicated by _
    current_board = [];
    for x in randomword:
        current_board.append("_")

    while (tries_left > 0 and player_has_won == False):
        for letter in current_board:
            print("%s" % (letter), end =" ")
        if len(guessed_letters) > 0:
            print("\nThese are the letters you have already guessed")
            for letter in guessed_letters:
                print("%s" % (letter), end =" ")

        print("\nYou have %d tries remaining" % (tries_left))

        user_guess = input("Please guess a letter: ")

        user_guess = user_guess.lower()
        
        if len(user_guess) > 1:
            print("You can only guess one character at a time\n")
            continue

        elif len(findArr(guessed_letters, user_guess)) > 0:
            print("You have already guessed this letter\n")
            continue

        else:
            guessed_letters.append(user_guess)
            indexes = findArr(randomword, user_guess)
            if len(indexes) == 0:
                print ("\n\nThe letter %s is not in the word" % (user_guess))
                tries_left = tries_left - 1
            else:
                for index in indexes:
                    current_board[index] = randomword[index]

        if (len(findArr(current_board, "_")) == 0):
            player_has_won = True

    if player_has_won:
        print("Congratulations. You won! The word was %s" % (randomword))
    else:
        print("The word was %s" % (randomword))
        print("%s\n" % (randomshades[randint(0, len(randomshades))]))

def run():
    randomword = getrandomword()
    print("Lets play hangman!")
    playhangman(randomword)

run()
