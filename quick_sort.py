def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]    # "for each element x in arr, include x in the new list".
    middle = [x for x in arr if x == pivot] # "for each element x in arr, include x in the new list".
    right = [x for x in arr if x > pivot]   # "for each element x in arr, include x in the new list".
    return quicksort(left) + middle + quicksort(right)  #recursion


newArray = [1, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 3, 4, 5, 4, 3]

sortedArray = quicksort(newArray)

print(sortedArray)


#Recursion example

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120