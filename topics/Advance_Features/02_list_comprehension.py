""" 
Ternary Operator
<true code> if <condition> else <false Code> 

Example:
i**2 if i**2 > 9 else None
"""

""" 
list comprehension
<loop_inside_code> for <iterable_object> in <iterator> <condition_on_iterable>

Example:
i for i in range(11) if i % 2 == 0
"""

# List Comprehension With Ternary Operator
print("Example 1:")
print(*(i**2 if i**2 > 9 else None for i in range(11) if i % 2 == 0))

# Above Example With For Loop and If...Else
print("\n Example 2:")
for i in range(11):
    if i % 2 == 0:
        if i**2 > 9:
            print(" ",i**2)
    else:
        continue