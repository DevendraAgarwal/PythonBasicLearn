
def check_list(myList: list):
    asc = False
    desc = False
    for i in range(len(myList)-1):
        if (myList[i] < myList[i+1]):
            asc = True
        elif(myList[i] > myList[i+1]):
            desc = True
            
    if (asc and desc):
        return "Unordered List"
    elif(asc and (not desc)):
        return "Ascending Ordered List"
    elif((not asc) and desc):
        return "Descending Ordered List"
    
print(check_list([4,2,1,5]))
print(check_list([4,2,1,0]))
print(check_list([1,2,4,5]))