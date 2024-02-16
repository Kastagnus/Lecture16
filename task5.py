# დავალება 1

mystring = input("შეიყვანე ტექსტი და მე დაგიბრუნებ UTF-8 ფორმატით: ")
print(mystring.encode('utf-8'))

# დავალება 2

newstring = input("შეიყვანეთ წინადადება: ").strip().lower()
if "python" in newstring:
    print(newstring.replace("python", "Python") + "\nPython")

else:
    print(newstring + "\nPython")

# დავალება 3

text = input("გთხოვთ შეიყვანოთ წინადადება: ")
print(text.strip()[:len(text) // 2])

# დავალება 4
import string

newtext = input("გთხოვთ შეიყვანოტ ტექსტი: ")
valid1 = string.ascii_letters
valid2 = string.digits
valid3 = string.whitespace
valid4 = valid1 + valid2 + valid3

digit_count = 0

for x in newtext.strip():

    if x not in valid4:
        print("არავალიდურია !")
        break
    elif x in valid2:
        digit_count += 1
        continue
    else:
        continue
else:
    if digit_count == 1:
        print("ვალიდურია !")
    else:
        print("არავალიდურია !")

# დავალება 5


newstring = input("შიყვანეთ ტექსტი: ")

bytes_newstring = newstring.encode()
print("ბაიტებში:", bytes_newstring)

decoded_newstring = bytes_newstring.decode()
print("ორიგინალი ტექსტი:", decoded_newstring)
