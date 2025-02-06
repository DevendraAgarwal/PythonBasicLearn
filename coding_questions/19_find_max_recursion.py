lis = [1,4,16,7,10,20]

max_number = 0
def find_max(l, max_number):
    if max_number < l[0]:
        max_number = l[0]
    if len(l) == 1:
        return max_number
    return find_max(l[1:], max_number)
    
print(find_max(lis, max_number))