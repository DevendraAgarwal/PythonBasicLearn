'''
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''

def remove_duplicates(arr):
    
    seen = set()
    filter_list = []
    for num in arr:
        if num not in seen:
            filter_list.append(num)
            seen.add(num)
    return filter_list

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))