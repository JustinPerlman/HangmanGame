import random

def underline(word):
    length = len(word)
    underlines = []
    for lp in range(0, length, 1):
        underlines.append("_ ")
    print("")
    print(''.join(underlines))
    return underlines


def game():
    wordeasy = ["cat", "mom", "dig", "run", "oil", "rock", "trap", "city"]
    wordmedium = ["rabbit", "trash", "reward", "morning", "million", "track", "trend", "tired"]
    wordhard = ["triad", "mortgage", "colonel", "meteor", "context", "literal", "silicon", "pendulum"]
    difficulty = str.lower(input("Choose Level: Easy, medium, or hard "))
    wordnum = random.randint(0, 7)
    if difficulty == "easy":
        word = wordeasy[wordnum]
    if difficulty == "medium":
        word = wordmedium[wordnum]
    if difficulty == "hard":
        word = wordhard[wordnum]
    print("")
    lives = 10
    underlines = underline(word)
    guessed = []
    guesser(word, underlines, lives, guessed)


def guesser(word, underlines, lives, guessed):
    if lives > 0:
        length = len(word)
        print("Incorrect Letters: " + str(guessed))
        letter1 = input("Guess letter!")
        findcount = 0
        cheatcode(letter1)

        for lp in range(0, length, 1):
            if word[lp] == letter1:
                underlines[lp] = str(letter1)
                findcount = findcount + 1

        if findcount == 0:
            guessed.append(letter1)
            lives = lives - 1
        print("")
        print("")
        print("You found " + str(findcount) + " letters.")
        print(str(lives) + " lives left.")
        print("")
        print(''.join(underlines))
        print("")
        if ''.join(underlines) == word:
            print("YOU WIN!!")
            print("Your word was " + str.upper(word) + ". You used " + str(10 - lives) + " lives.")
            playagain()

        else:
            guesser(word, underlines, lives, guessed)
    else:
        print("YOU LOSE! GO READ A DICTIONARY!")
        print("Your word was " + word + "!")
        playagain()


def playagain():
    again = str.lower(input("Would you like to play again? Y or N:"))
    if again == "n":
        print("GAME OVER!")
        print("")
        again = str.lower(input("WAIT! Are you sure? Do you want to play again? Y or N"))

    if again == "y":
        print("")
        print("Another round it is!")
        print("")
        game()


def cheatcode(letter1):
    if letter1 == "Tempest":
        print("CHEAT CODE ENTERED. You win.")
        playagain()

    if letter1 == "tempest":
        for lp in range(0, 1000000):
            print("SECURITY COMPROMISED")
            # win = GraphWin("ERROR", 1000, 500)
            # text = Text(Point(500, 250), "ERROR")
            # text.setFace("arial")
            # text.setSize(30)
            # text.setStyle("bold")
            # text.draw(win)


game()

