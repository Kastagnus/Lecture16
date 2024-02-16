import random

# დავალება 1

number = eval(input("გთხოვთ შეიყვანოთ რიცხვი: "))
sum = 0

for x in range(0,number):
    sum += x

print(sum)

# დავალება 2

number = eval(input("გთხოვთ შეიყვანოთ რიცხვი: "))

while number != 0:
    number -= 1
    print(number + 1)

# დავალება 3

import random
correct = True

number = random.randint(1,100)
while correct:

    number_by_player = eval(input("გთხოვთ შეიყვანოთ ციფრი ერთიდან ასამდე: "))

    if number_by_player < number:
        print("უპს! ჩაფიქრებული ციფრი მეტია შენ ციფრზე ")
        continue
    elif number_by_player > number:
        print("უპს! ჩაფიქრებული ციფრი ნაკლებია შენ ციფრზე ")
        continue
    else:
        print("გილოცავ! შენ სწორად გამოიცანი")
        break



# დავალება 4

total_sum = 0
running = True

while running:
    data = input("შეიყვანეთ ციფრი ან sum: ")

    if data == "sum":
        print(f"შეყვანილ დადებით ციფრთა ჯამია: {total_sum}")
        break
    elif eval(data) > 0:
        total_sum += eval(data)
        continue
    elif eval(data) < 0:
        continue

















