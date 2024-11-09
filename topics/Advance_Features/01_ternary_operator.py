'''
Syntax:

<value_if_true> if <condition> else <value_if_false>
'''

x = 5
y = 3

result = "Greater" if x > y else "Less or Equal"

print(result)  # Output: "Greater"

name = None
name = "John" if name else "Anonymous"
print(name)  # Output: "John"