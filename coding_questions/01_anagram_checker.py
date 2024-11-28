# Method 1
def are_anagrams1(str1, str2):
    return sorted(str1) == sorted(str2)

# Method 2
from collections import Counter

def are_anagrams2(str1, str2):
    return Counter(str1) == Counter(str2)


print(are_anagrams1("listen", "silent"))  # True
print(are_anagrams1("hello", "world"))  # False

print(are_anagrams2("listen", "silent"))  # True
print(are_anagrams2("hello", "world"))  # False