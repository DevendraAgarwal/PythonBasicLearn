def second_max_value(lis):

    if len(lis) < 2:
        return None
    
    max1 = max2 = float('-inf')
    for val in lis:
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2 and val != max1:
            max2 = val
    return max2

lis = [1,3,5,2,4,10,11]
print(second_max_value(lis))