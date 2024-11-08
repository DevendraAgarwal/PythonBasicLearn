# Dictionary

""" 
{} Declare Using Same Like Set
dict() Declare Using Same Like Set

-> It has Key Value Pair unlike Set (Json) (Associative Array)
-> "key" = "Value"
"""

dic1 = dict()
dic1['name'] = "Shaktimaan"
print(dic1)

dic1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic1)

dic = {
    "name" : "Mr. India",
    "profession": "Chor"
}
print(dic)

print(dic.keys())

print(dic.values())

dic_copy = dic.copy()
print(dic_copy)

dic_copy['name'] = "Natwarlal"
print(dic)
print(dic_copy)