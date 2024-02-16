arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble(arr)
print("Sorted list:", arr)

def mergesorting(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        first = arr[:mid]
        second = arr[mid:]

        mergesorting(first)

        mergesorting(second)

        i = j = k = 0

        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                arr[k] = first[i]
                i += 1
            else:
                arr[k] = second[j]
                j += 1
            k += 1

        while i < len(first):
            arr[k] = first[i]
            i += 1
            k += 1

        while j < len(second):
            arr[k] = second[j]
            j += 1
            k += 1

mergesorting(arr)
print("Sorted with merge:", arr)

def insertion(arr):

    for i in range(1, len(arr)):
        agent = arr[i]
        j = i-1
        while j >=0 and agent < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = agent


insertion(arr)
print("Sorted with insertion:", arr)

