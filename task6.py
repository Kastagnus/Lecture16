# დავალება 1



mylist = []

def myfunction(command, number = 0):

    if command == "a":
        mylist.append(int(number))
    elif command == "r":
        mylist.remove(int(number))

run = True
while run:

    entrant = input("შეყვამე ბრძანება და რიცხვი (გამოყავი მძიმით). \nბრძანებები: a - სიაში დამატება, r - სიიდან წაშლა, e - სიის გამოტანა: ")
    if entrant == "e":
        print(mylist)
        break
    else:
        command, number = entrant.split(",")
        myfunction(command, number)

# დავალება 2

my_list = [43, '22', 12, 66, 210, ["hi"]]

print(my_list.index(210))
my_list[-1].append("hello")
my_list.pop(2)
print(my_list)
mylist2 = my_list.copy()
mylist2.clear()
print(my_list)
print(mylist2)

# დავალება 3

import re

def checknumber(number):

    pattern = r'\(\d{3}\) \d{3}-\d{4}'

    if re.match(pattern,number):
        return True
    else:
        return False

num = "(345) 678-9876"

answer = checknumber(num)
print(answer)
