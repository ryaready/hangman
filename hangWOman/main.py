# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random
import time
print ("welcome to hangWOman" )
name = input("what's ur name chica:")
print ("welcome " + name+ " to my lair")
time.sleep(2)
print("you're time is coming")
time.sleep(2)
def main():
    global count
    global display
    global word
    global guessed
    global length
    global play
    global gender
    words= ["beach","yoga","meditation","film","journal","apocalypse","friends","wind","mitski","sunny","plants"]
    word = random.choice(words)
    length = len(word)
    count = 0
    display = '_' * length
    guessed = []
    play = ""
gender = input("are you a woman? y = yes, n = no \n")
while gender not in ["y", "n","Y","N"]:
    gender = input("are you a woman? y = yes, n = no \n")
if gender == "y":
    main()
elif gender == "n":
    print("NO MEN ALLOWED")
    exit()
def play_loop():
    global play
    play = input("play again? y = yes, n = no \n")
    while play not in ["y", "n","Y","N"]:
        play = input("Do You want to play again? y = yes, n = no \n")
    if play == "y":
        main()
    elif play == "n":
        print("We expect you back again muahahaha")
        exit()
def hangman():
    global count
    global display
    global word
    global guessed
    global play
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",guessed,word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()