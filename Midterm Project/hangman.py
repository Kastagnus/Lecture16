#მომხმარებლისგან ვიღებთ ინფუთს
#ვამოწმებთ რომ ერთი სიმბოლოა
#ვამოწმებთ რომ სტრინგია
import random

word_list = ["shipment", "battleship", "cargo", "flower", "accounting", "hearless", "batmobile", "blackboard", "shoulders"]
word = random.choice(word_list)
def ask_input():
    while True:

        letter = input("Enter a letter: ")
        if len(letter) == 1 and letter.isalpha():
            return letter.lower()
        else:
            print("invalid character")

def display(word):
    num_letters = len(word)
    print("_"*num_letters)

def display_2(word, letter=None):
    charlist = []
    for char in word:
        charlist.append("_")
    if letter == None:
        print("Welcome to hangman! ")
        print("".join(charlist), end="")
    # elif letter is not None:
    elif letter in word:
        indicies = lambda word, letter: [i for i, char in enumerate(word) if char == letter]
        print(indicies(word, letter))
        for i in indicies(word, letter):
            charlist[i] = letter
        print("".join(charlist), end="")
    else:
        print("try again")

display_2("aascii")








