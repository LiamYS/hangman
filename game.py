import random

class Player():
    def __init__(self, name):
        self.name = name
        self.lives = 9

class Word():
    def __init__(self, string):
        self.string = list(string)
        self.word = list("-" * len(self.string))

    def showLetter(self, letter):
        if letter in self.string:
            self.word[self.string.index(letter)] = letter
            return "".join(self.word)
        else:
            return False

words = {
    1: "python",
    2: "torn",
    3: "agreement",
    4: "certainly",
    5: "government",
    6: "management",
    7: "professional",
    8: "significant",
    9: "weapon",
    10: "honorificabilitudinitatibus"
}

p1 = Player("")
hangmanword = Word(words[random.randint(1,10)])
guessedList = []

print("""HANGMAN | a Python game by Liam
------------------------------------------------
This is a singleplayer version of the original hangman game.
You start with nine lives, a random word from a list is chosen
by the computer. If you guess the wrong letter a live gets taken off.
------------------------------------------------\n""")
while True:
    p1 = Player(input("Enter name for P1: "))
    if len(p1.name) < 1:
        print("That is not a real name, is it!\n")
        continue
    else:
        break
    
print(f"{p1.name} the game begins, goodluck!\n")
print(f"The word contains {len(hangmanword.string)} letter: {''.join(hangmanword.word)} \n")

running = True
while running:
    if p1.lives <= 0:
        gameover = input("You lost the game! Type 'EXIT' to stop playing: ")
        if gameover.upper() == "EXIT":
            running = False
        else:
            p1.lives = 9
            guessedList = []
            hangmanword = Word(words[random.randint(1,10)])
            while True:
                p1 = Player(input("Enter name for P1: "))
                if len(p1.name) < 1:
                    print("That is not a real name, is it!\n")
                    continue
                else:
                    print(f"{p1.name} the game begins, goodluck!\n")
                    print(f"The word contains {len(hangmanword.string)} letter: {''.join(hangmanword.word)} \n")
                    break
            continue

    while True:
        guessedLetter = input("Guess a letter: ")
        if len(guessedLetter) > 1:
            print("That's more than one letter!")
            continue
        else:
            if not hangmanword.showLetter(guessedLetter):
                guessedList.append(guessedLetter)
                p1.lives -= 1
                print("\nWRONG!")
                print(f"{p1.name} has {p1.lives} lives left!")
                print(f"Letters tried: {', '.join(guessedList)} \n")
                break
            else:
                print(f"That letter was part of the word, good job!")
                print(f"{hangmanword.showLetter(guessedLetter)} \n")
                break