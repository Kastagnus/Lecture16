# # დავალება 1

int_list = []

def addnumber(n):
    int_list.append(n)

    return int_list

print(addnumber(5))
print(addnumber(6))

# # დავალება 2

def sumlist(list):

    i = 0
    for x in list:
        i += x
    return i

list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(sumlist(list))

# # დავალება 3

gl_str = "global"

def makelocal():

    gl_str = "local"
    return gl_str

print(makelocal())
print(gl_str)
#
# # დავალება 4
#
def sumdigits(number):

    if number < 10:
        return number
    else:
        return number % 10 + sumdigits(number // 10)

number = 1234
print(sumdigits(number))

# დავალება 5
def reversestring(x):

    if len(x) <= 1:
        return x
    else:
        return reversestring(x[1:]) + x[0]

reversestring("hello")



