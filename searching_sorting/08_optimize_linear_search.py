def linear_search(arr, target):
    last = len(arr) - 1
    mid = last // 2
    counter = 0

    for i in range(len(arr)):
        counter += 1

        if arr[i] == target:
            return i, counter
        if arr[last] == target:
            return last, counter
        if arr[mid-counter] == target:
            return mid-counter, counter
        if arr[mid+counter] == target:
            return mid+counter, counter
        if i > mid-counter:
            return -1, counter # not found
        
        last -= 1
        
    return -1, counter  # not found

numbers = [12, 7, 19, 3, 15, 25, 8, 10, 42, 56, 77, 23, 89, 65, 33, 99, 100]
target = 10
result, loop_trips = linear_search(numbers, target)
print(result, loop_trips)  # Output: 7 , 1