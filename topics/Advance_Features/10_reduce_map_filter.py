'''
reduce

reduce applies a rolling computation to sequential pairs of values in a list, 
returning a single output. It’s often used for aggregations, such as summing or 
multiplying a list of numbers.

Use:
Calculating sums, products, or averages of a list of numbers
Combining strings or lists using a custom operation
'''

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

'''
map

map applies a function to each element of an iterable, returning a new iterable 
with the transformed values.

Use:
Transforming data (e.g., converting strings to uppercase or integers to squares)
Applying a function to each element of a list or other iterable
'''

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

'''
filter

filter creates a new iterable with only the elements for which a given function 
returns True.

Use:
Filtering out unwanted values (e.g., removing odd numbers or non-numeric values)
Selecting specific elements based on a condition
'''

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


'''
Additional Tips

1. map, filter, and reduce can be used with lambda functions or regular functions.
2. When using map or filter, you may need to convert the output to a list or other 
    iterable, depending on the context.
3. reduce is not a built-in Python function in Python 3; you need to import it from the functools module.

Real-World Examples

Data processing:
    Use map to transform a list of strings to uppercase, and then filter to 
    remove empty strings.

Financial calculations:
    Use reduce to calculate the total value of a list of transactions, and 
    then map to apply a discount percentage to each transaction.

Data cleaning:
    Use filter to remove rows from a dataset with missing values, and then map 
    to apply a custom function to clean the data.
'''