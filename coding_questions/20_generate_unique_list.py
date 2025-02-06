import random

def get_unique_list(length):
    lst = set()
    while True:
        if len(lst) == length:
            break
        item = random.randint(1,100)
        lst.add(item)
    return list(lst)

print(get_unique_list(5))