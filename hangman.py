import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

print("welcowome to hung manuwu")

word = input("What is the word? ")
allowed_fails = input("How many fails allowed? ")
badletters = []
x = allowed_fails
while int(x) > 0:
    clear_screen()
    if len(badletters) > 0: print("Bad letters guessed", *badletters, sep=", ")
    print("Number of tries left " , x)
    guess = input("Guess a letter ")
    if guess in word:
        print("good")
    else:
        print("bad")
        x = int(x) - 1
        badletters.append(guess)
    print(x)
