# Set

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

# delete object from Set, It will Not KeyError Exception When Element not Present
s.remove(100)
print(s)