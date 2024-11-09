# Dictionary

""" 
{} Declare Using Same Like Set
dict() Declare Using Same Like Set

-> It has Key Value Pair unlike Set (Json) (Associative Array)
-> "key" = "Value"
"""

'''
Creating a Dictionary
You can create a dictionary in Python using the following methods:

Brace notation:
    my_dict = {'key1': 'value1', 'key2': 'value2'}

Dict constructor:
    my_dict = dict([('key1', 'value1'), ('key2', 'value2')])

Dict comprehension:
    my_dict = {k: v for k, v in [('key1', 'value1'), ('key2', 'value2')]}
'''

'''
Use Case Of Dictionary

Configuration files:
    Store configuration settings as key-value pairs.

Data storage:
    Use dictionaries to store and manipulate data in a flexible and efficient manner.

Caching:
    Use dictionaries to cache frequently accessed data.
'''

dic1 = dict()
dic1['name'] = "Shaktimaan"
print(dic1)

dic1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic1)

dic = {
    "name" : "Mr. India",
    "profession": "Chor"
}
print(dic)

print(dic.keys())

print(dic.values())

dic_copy = dic.copy()
print(dic_copy)

dic_copy['name'] = "Natwarlal"
print(dic)
print(dic_copy)