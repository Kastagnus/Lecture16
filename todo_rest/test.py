# def cloudjump(c, k):
#     e = 100
#     multiplier = lambda c, k: 1 if len(c) % k == 0 else len(c) // k
#     res = multiplier(c,k)
#     c1 = c * res
#     jumps = len(c1) / k
#     j = 0
#     for _ in range(0, int(jumps)):
#         if c1[j] == 0:
#             e -= 1
#         else:
#             e -= 3
#         j += k
#     return e

# def finddigits(n):
#     poss_divisors = [int(x) for x in str(n)]
#     divisors = []
#     for i in poss_divisors:
#         if i != 0 and n % i == 0:
#             divisors.append(i)
#     return len(divisors)

# def factorial(num):
#
#     res = 1
#     for i in range(1, num+1):
#         res *= i
#     return res
'aba'
import math

'abaaaa'


# def appendanddelete(s, t, k):
#     max_needed = len(s) + len(t)
#     common = 0
#     for i in range(0, min(len(s), len(t))):
#         if s[i] == t[i]:
#             common += 1
#         else:
#             break
#     diff1 = len(s) - common
#     diff2 = len(t) - common
#     min_needed = diff1 + diff2
#     k_range1 = range(min_needed, max_needed, 2)
#     k_range2 = range(max_needed, 101)
#     print(k_range1, k_range2)
#     for i in k_range1:
#         print(i)
#     print(2 in k_range1)
#     if k in k_range1 or k in k_range2:
#         return True
#     else:
#         return False
#
#
# s = 'ashley'
# t = 'ash'
#
# k = 2
# print(appendanddelete(s, t, k))

# def findsqr(a,b):
#     start = math.ceil(math.sqrt(a))
#     end = math.floor(math.sqrt(b))
#     if end >= start:
#         return end - start + 1
#     else:
#         return 0
#
# a = 298101393
#
# b = 884597840
#
# print(findsqr(a,b))


# def libraryFine(d1, m1, y1, d2, m2, y2):
#     year_diff = y1 - y2
#     month_diff = m1 - m2
#     day_diff = d1 - d2
#     if year_diff > 0:
#         return 10000
#     if year_diff == 0 and month_diff > 0:
#         return 500*month_diff
#     if year_diff == 0 and month_diff == 0 and day_diff > 0:
#         return 15*day_diff
#     return 0
#
# print(libraryFine(28,2,15,15,4,15))

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

def formmagigsqr(a):

    res1 = 0
    res2 = 0
    for i in range(0,3):
        res1 += a[i][0]
        res2 += a[i][2]

    print(res1, res2)


formmagigsqr(s)






