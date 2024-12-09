s= 'madam'

def is_palindrome(s):
    return s == s[::-1]

is_palindrome = lambda s: s.lower() == "".join(reversed(s.lower()))

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")