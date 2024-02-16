# დავალება 1

list1 = [1,2,3]
list2 = ["a", "b", "c"]
newlist = list(zip(list1, list2))
print(newlist)

# დავალება 2

from functools import reduce

multiply_list = lambda nums: reduce(lambda x, y: x * y, nums, 1)

while True:
    try:
        list_input = input("Enter a list of numbers: ")
        numbers = [float(num) for num in list_input.split()]

        result = multiply_list(numbers)

        print("Multiplication of all numbers:", result)
        break

    except TypeError:
        print("Invalid input! Please enter again")
    except ValueError:
        print("Invalid input! Please enter again")

# დავალება 3


filter_odd_nums = lambda nums: list(filter(lambda x: x % 2 != 0, nums))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_odd_nums(numbers)

print("Odds from list:", result)

# დავალება 4

words = [["running ", "Jumping", "coding", "swimming", "hiking"], "ing"]

def filter_words(x,y):

    filtered = list(filter(lambda x: x.endswith(y), x))
    return filtered

result = filter_words(words[0],words[1])


print(f"Strings ending with {words[1]}:", result)

