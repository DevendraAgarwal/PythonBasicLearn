# lambda Function

""" 
lambda <1st param>, <2nd Param>: <code block>
"""

add = lambda a, b: a + b
print(add(5,9))

lst = [10,20,30,40,50,200,60,500,70,80,90]
sorted_numbers = sorted(lst, key=lambda x: x > 100)
print(sorted_numbers)
