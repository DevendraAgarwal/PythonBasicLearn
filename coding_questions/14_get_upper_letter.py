str = 'abcABC'
upper = []

def get_upper_letter_short(str):
    return [i for i in str if i.isupper()]

def get_upper_letter(str):
    for i in str:
        if i >= 'A' and i <= 'Z':
            upper.append(i)
    return upper

print(get_upper_letter(str)) # ['A', 'B', 'C']