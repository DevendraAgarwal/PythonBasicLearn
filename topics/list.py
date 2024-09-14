# list

""" 
[] Define By This 
-> Same or Different Type Object can store in list
"""

lst = ['a', 2, 67, "Name", 6.5]
print(lst)

lst.append(89)
print(lst)

""" 
lst.append([67, 'test'])
OUTPUT-> ['a', 2, 67, 'Name', 6.5, 89, [67, 'test']]
"""

lst.extend([67, 'test'])
print(lst)

lst.reverse()
print(lst)

lst.remove(67)
print(lst)

lst.insert(3, "insertTest")
print(lst)

print("Count of Value 67 in List: ",lst.count(67))
print("Length Of List: ",len(lst))