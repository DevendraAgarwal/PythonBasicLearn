'''
In Python, strings are used to represent textual data. 
A string is a sequence of characters enclosed in either single quotes (') 
or double quotes ("). Here are some key aspects of Python strings:

Immutable: Strings are immutable, meaning they cannot be changed after creation.
    To modify a string, you need to create a new string.

Indexing: Strings can be indexed using square brackets []. 
    Indexing starts from 0, so s[0] refers to the first character, 
    s[1] to the second, and so on.

Slicing: You can extract a subset of characters from a string using slice notation,
    e.g., s[1:3] returns the characters at indices 1 and 2.

Concatenation: Strings can be concatenated using the + operator or the str.format() method.

Methods: Python strings have various built-in methods, such as:
    lower(), upper(), title(), and swapcase() for case manipulation
    strip(), lstrip(), and rstrip() for removing whitespace
    split() and join() for splitting and joining strings
    replace() for replacing substrings
    find() and index() for searching substrings

Raw Strings: Raw strings are prefixed with an r and treat backslashes (\) as 
    literal characters, rather than escape characters.

Unicode: Python 3.x uses Unicode strings by default, which support characters 
    from various languages and scripts. You can also work with byte strings 
    (denoted by the b prefix) for compatibility with older code.
'''

'''
Format Specification Mini-Language

Python’s str.format() method uses a mini-language to specify how to format strings.
Here are some common format specifiers:

d: Decimal integer
f: Fixed-point number
g: General format (auto-choose between fixed-point and scientific notation)
o: Octal integer
x: Hexadecimal integer (lowercase)
X: Hexadecimal integer (uppercase)
s: String
%: Percentage
'''

# String Function 

name = "Hello shaktimaan"
print(name)

# Return a New String as Output
new = name.replace("Hello", "Sorry")
print(new)

new = name.upper()
print(new)

new = name.lower()
print(new)

new = name.title()
print(new)

# Return List
new = name.split(" ")
print(new)

new = name.count("a")
print(new)

# In case String not Found It not Raise Exception Rather Return -1
new = name.find("jiHello")
print(new)

# It Raise Exception 
new = name.index("shakti")
print(new)

new = name.islower()
print(new)

name = "hello shaktimaan"
new = name.islower()
print(new)