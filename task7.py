# დავალება 1

def sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(2, n+1):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


print(sequence(10))

# დავალება 2
def anagrams(word1, word2):
    # Remove non-letter characters and convert to the same case
    newword1 = ''.join(char.lower() for char in word1 if char.isalpha())
    newword2 = ''.join(char.lower() for char in word2 if char.isalpha())


    return sorted(newword1) == sorted(newword2)

print(anagrams("listen", "silent"))
print(anagrams("hello", "world"))

# დავალება 3

def factorial(n):
    if n < 0:
        return "No factorial "
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# დავალება 4

def counting(string, symbol):

    return string.count(symbol)


print(counting("Hellllo!, worllld!", "l"))




