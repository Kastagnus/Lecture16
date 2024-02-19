# მომხმარებლისგან ვიღებთ ინფუთს
# ვამოწმებთ რომ ერთი სიმბოლოა
# ვამოწმებთ რომ სტრინგია
import random

word_list = ["shipment", "battleship", "cargo", "flower", "accounting", "heartless", "batmobile", "blackboard",
             "shoulder"]


def welcome_and_display(limit, word):
    print(f"Welcome to the game hangman, you have {limit} tries to guess the hidden word !")
    num_letters = len(word)
    print("_" * num_letters)


def ask_input():
    while True:

        letter = input("\nEnter a letter: ")
        if letter.isalpha():
            return letter.lower()
        else:
            return None

def display(word):
    num_letters = len(word)
    print("_" * num_letters)


def start_game():
    word = random.choice(word_list)
    limit = 7
    welcome_and_display(limit, word)

    def check_limit(limit):

        if limit == 4:
            print(f"\nCareful! you have to guess it quickly! only {4} attempts remaining")
        elif limit == 1:
            print("\nThe last attempt!")
        elif limit == 0:
            print("\nout of attempts!")
        else:
            print(f"\nYou have {limit} attempts left")

    charlist = []
    used_letters = []
    for _ in word:
        charlist.append("_")
    while limit > 0:
        letter = ask_input()

        if letter is not None and len(letter) == 1 and letter in word and letter not in used_letters:
            indicies = lambda word, letter: [i for i, char in enumerate(word) if char == letter]
            for i in indicies(word, letter):
                charlist[i] = letter
            if "_" not in charlist:
                print(f"Congratulations! You won!, correct word is {word}")
                limit -= limit
                return True
            print("Wow! You have guessed the letter correctly")
            print("".join(charlist), end="")
            used_letters.append(letter)
        elif len(word) > 1 and letter == word:
            limit -= limit
            print(f"Congratulations! You won, correct word is {word}")
            return True
        elif letter in used_letters:
            print(f"You already used letter: {letter}, please choose another one")
            print(f"used characters are: {used_letters}")
        elif letter is None:
            print(f"Wrong input! please provide only alphabet characters")
            check_limit(limit)
        elif len(letter) > 1 and len(letter) != len(word):
            print(f"You can only write 1 letter or the full word, try again !")
            print("".join(charlist), end="")
        else:
            used_letters.append(letter)
            limit -= 1
            if limit > 0:
                print("Wrong Shot! try again <3")
                print("".join(charlist), end="")
            else:
                print("Sorry, game is over!")
                return True

            check_limit(limit)

def run():

    while True:
        finished = start_game()
        if finished:
            while True:
                ask_again = input("Do you want to play again? yes or no: ")
                if ask_again.isalpha() and ask_again.lower() == "yes":
                    break
                elif ask_again.isalpha() and ask_again.lower() == "no":
                    print("Thank you for playing! Goodbye ! ")
                    return
                else:
                    print("Please enter yes or no")

run()
