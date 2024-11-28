# Set

'''
Key Characteristics:

Unordered:
    Sets do not maintain any order of elements.

Unique elements:
    Sets automatically remove duplicates, ensuring each element appears only once.

Mutable:
    Sets can be modified after creation by adding or removing elements.

Hashable:
    Sets use hash tables for fast membership testing and set operations.
'''

""" 
{} Use this for Declare

-> There is No Key Value Pair
-> Every Object should be unique
-> Unordered Value
"""

s = {124, "b"}
print(s)

s.add(123)
print(s)

# b already present in the Set so it will not add twice
s.add('b')
print(s)

# delete object from Set, It will Not Raise KeyError Exception
s.discard(124)
print(s)

s.add(100)
print(s)

# delete object from Set, It will Raise KeyError Exception When Element not Present
s.remove(100)
print(s)

'''
Frozen Sets:

Frozen sets are immutable versions of sets. They can be created using the 
frozenset() function and are useful when you need to ensure the set remains 
unchanged.
'''

frozen_set = frozenset({1, 2, 3})
print(frozen_set)  # frozenset({1, 2, 3})

try:
    frozen_set.add(4)
except AttributeError:
    print("Frozen set cannot be modified")