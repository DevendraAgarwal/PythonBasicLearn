# Polymorphism

string = "This is my name"
print(len(string))

lst = [1, 3, 7]
print(len(lst))

dic = {
    "name" : "Python"
}
print(len(dic))

# Class Polymorphism

class main:
    
    def my_function(self, a: int, b: int = 5):
        if b == 5:
            return a**2
        
        return a+b
    
obj = main()

print(obj.my_function(4,6))
print(obj.my_function(4))