# დავალება 1

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
print("შეიყვანე რიცხვი და მე შევამოწმებ არის თუ არა ის ჩემ სიაში")
num = eval(input("საძიები რიცხვი: "))

if num in num_list:

    print("თქვენს მიერ შეყვანილი რიცხვი სიაშია")
else:
    print("თქვენს მიერ შეყვანილი რიცხვი სიაში არ არის")

# დავალება 2

print("ახლა კი შეიყვანე რიცხვი და მე შევამოწმებ ის კენტია თუ ლუწი ")
num1 = eval(input("საძიებო რიცხვი: "))

if num1 % 2:
    print("კენტია")
else:
    print("ლუწია")

# დავალება 3

st1 = "გამარჯობა"
st2 = "ნახვამდის"

if st1 is st2:
    print("Same object")
else:
    print("Not the same object")

# დავალება 4

num_list1 = [44, 23, 11, 8, 20, 56, 33, 55]

print("შეიყვანე რიცხვი და მე გავაკეთებ შედარებებს დათქმული პირობით")
num2 = eval(input("საძიებო რიცხვი: "))

if num_list1[2] < num2 < num_list1[-1]:
    print("More than list elements")
elif num2 == num_list1[5]:
    print("Equal")
else:
    print("None of the conditions were met")

