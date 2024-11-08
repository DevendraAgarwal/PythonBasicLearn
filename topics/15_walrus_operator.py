""" 
:=  This is Walrus Operator
"""

lst = [10,2,4,5,6]
i = -1
while (i := i +1) < (n := len(lst)):
    print(lst[i], n)