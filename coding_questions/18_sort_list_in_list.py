'''
input [2, 4 ,1, 2, 1,4,5,2,5]
output: [1, 1, 2, 2, 2, 4, 4, 5, 5]
--------------------------------
input [2, 4,1, 2,1,4,5,2,5, [5, 1,3,4]]

output: [1, 1, 2, 2, 2, 4, 4, 5, 5, [1,3,4,5]]
------------------------------------
input [[5, 1,3,4], 2, 4,1, 2,1,4,5,2,5]

output: [ [1,3,4,5], 1, 1, 2, 2, 2, 4, 4, 5, 5]
------------------------------------
input [1, 1, [5, 1,3,4], 2, 4,1, 2,1,4,5,2,5]

output: [1, 1, [1,3,4,5], 1, 1, 2, 2, 2, 4, 4, 5, 5]
'''

def sort_list(l):
    l.sort()
    return l
    
# lis = [2, 4 ,1, 2, 1,4,5,2,5]
lis = [2, 4,1, 2,1,4,5,2,5, [5, 1,3,4], 3,6,3]
# lis = [[5, 1,3,4], 2, 4,1, 2,1,4,5,2,5]
# lis = [1, 1, [5, 1,3,4], 2, 4,1, 2,1,4,5,2,5]

final_list = []
no_list = True
for index,item in enumerate(lis):
    if type(item) is list:
        
        no_list = False
        if index > 0:
            first_half = lis[0:index]
            final_list.extend(sort_list(first_half))
        
        sorted_list = sort_list(item)
        final_list.append(sorted_list)
        
        if index < len(lis):
            second_half = lis[index+1:len(lis)]
            final_list.extend(sort_list(second_half))
        
if no_list:
    final_list = sorted(lis)

print(final_list)