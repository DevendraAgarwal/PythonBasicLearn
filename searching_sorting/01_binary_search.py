'''
Binary search is an efficient algorithm for finding a target value within a 
sorted array. It works by repeatedly dividing the search interval in half until 
the target value is found or the interval is empty.

How Binary Search Works

Divide the search space: 
Divide the search space into two halves by finding the middle index “mid”.

Compare the middle element: 
Compare the middle element of the search space with the key.

Repeat the process: 
If the middle element is equal to the key, the search is successful. 
If the key is less than the middle element, repeat the process with the 
lower half of the array. If the key is greater, repeat the process with the 
upper half.

Time Complexity:
The time complexity of binary search is O(log2n), where n is the number of 
elements in the array.

Space Complexity:
The space complexity of binary search is O(1), as it only uses a constant amount 
of space to store the indices and the key.
'''

# ---------------------------------Method 1---------------------------
def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1

# Test array
arr = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# ---------------------------------Method 2---------------------------

def binary_search2(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search2(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")