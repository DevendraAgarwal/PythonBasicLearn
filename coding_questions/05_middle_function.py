'''
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

# Without Slice
def middle(lst):
    
    new_list = []
    last = len(lst) - 1
    for index in range(len(lst)):
        if index == 0 or index == last:
            continue
        
        new_list.append(lst[index])
    return new_list

def middle_with_slice(lst):
    return lst[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]
print(middle_with_slice(myList))  # [2,3]