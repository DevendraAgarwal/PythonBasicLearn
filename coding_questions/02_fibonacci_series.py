# Method 1
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Method 2
def fibonacci2(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci2(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Method 3
def fibonacci3(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci3(n-1, memo) + fibonacci3(n-2, memo)
    return memo[n]

print([fibonacci3(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Method 4
def fibonacci4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci4()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34