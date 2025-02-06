# word: aaabbccddddabbb   out:a3b2c2d4a1b3

my_word = 'aaabbccddddabbb'

def get_char(word):
    for char in word:
        yield char

string = ''
prev = str(next(get_char(my_word)))
counter = 0

for current in get_char(my_word):
    if current == prev:
        prev = current
        counter += 1
    elif current != prev:
        string += f"{str(prev)}{counter}"
        prev = current
        counter = 1
        
string += f"{str(prev)}{counter}"        
print(string)