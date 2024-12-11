def find_missing_number(a):
    n = len(a) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(a)
    missing_number = expected_sum - actual_sum
    return missing_number

a = [1, 2, 3, 5, 6]
missing_number = find_missing_number(a)
print(f"The missing number is: {missing_number}")