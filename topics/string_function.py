# String Function 

name = "Hello shaktimaan"
print(name)

# Return a New String as Output
new = name.replace("Hello", "Sorry")
print(new)

new = name.upper()
print(new)

new = name.lower()
print(new)

new = name.title()
print(new)

# Return List
new = name.split(" ")
print(new)

new = name.count("a")
print(new)

# In case String not Found It not Raise Exception Rather Return -1
new = name.find("jiHello")
print(new)

# It Raise Exception 
new = name.index("shakti")
print(new)

new = name.islower()
print(new)

name = "hello shaktimaan"
new = name.islower()
print(new)