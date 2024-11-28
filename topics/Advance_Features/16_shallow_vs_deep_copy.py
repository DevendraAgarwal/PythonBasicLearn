# Shallow Copy

import copy

original_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)

print(shallow_copy)  # Output: [[1, 2], [3, 4]]

# Modify an element in the shallow copy
shallow_copy[0][0] = 10

print(original_list)  # Output: [[10, 2], [3, 4]]


# Deep Copy

original_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)

print(deep_copy)  # Output: [[1, 2], [3, 4]]

# Modify an element in the deep copy
deep_copy[0][0] = 10

print(original_list)  # Output: [[1, 2], [3, 4]]