nested_dict = {
   'a': 1,
   'b': {
       'c': 2,
       'd': {
           'e': 3,
           'f': 4
       }
   },
   'g': {
       'h': 5
   }
}

'''
Output: 
{
   'a': 1,
   'b_c': 2,
   'b_d_e': 3,
   'b_d_f': 4,
   'g_h': 5
}
'''
def parse_dict(root_key, dic):
    if type(dic) == dict:
        for k in dic:
            (key, value) = parse_dict(k, dic[k])
    
    if type(dic) != dict:
        return (root_key, dic)
        
    return (f"{root_key}_{key}", value)

output = {}
for key in nested_dict:
        (k, value) = parse_dict(key, nested_dict[key])
        output[k] = value
    
print(output)