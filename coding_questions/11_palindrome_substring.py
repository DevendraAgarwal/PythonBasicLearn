all_substr = []

def is_palindrome(s):
    return s == s[::-1]

def find_substring_palindrome(str):
    
    if (len(str) == 1):
        return False
    else:
        if is_palindrome(str):
            all_substr.append(str)
    
    find_substring_palindrome(str[0:-1])
    find_substring_palindrome(str[1:])

str = 'babad'
find_substring_palindrome(str)
print(all_substr)