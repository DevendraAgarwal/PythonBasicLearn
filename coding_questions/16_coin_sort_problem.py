num = 46
dic = {"10": 0, "5": 0, "2": 0, "1": 0}

while (num != 0):
    print(num)
    if num >= 10:
        div = num // 10
        dic["10"] = dic['10']+div 
        num = num - (10*div)
        continue
    if num >= 5:
        div = num // 5
        dic['5'] = dic['5']+div 
        num = num - (5*div)
        continue
    if num >= 2:
        div = num // 2
        dic['2'] = dic['2']+div 
        num = num - (2*div)
        continue
    if num == 1:
        dic['1'] = dic['1']+1 
        num = num - 1

print(dic)