'''
Linear search, also known as sequential search, is a simple searching algorithm 
that checks each element in a list or array sequentially until it finds the 
target element. It is the most basic searching algorithm and has a time 
complexity of O(n), where n is the number of elements in the list.
'''

# ---------------------------------Method 1-----------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found

numbers = [12, 7, 19, 3, 15, 25, 8, 10, 42, 56, 77, 23, 89, 65, 33, 99]
target = 25
result = linear_search(numbers, target)
print(result)  # Output: 5

# ---------------------------------Method 2-----------------------------

def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1  # not found
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

numbers = [12, 7, 19, 3, 15, 25, 8, 10, 42, 56, 77, 23, 89, 65, 33, 99]
target = 25
result = linear_search_recursive(numbers, target)
print(result)  # Output: 5