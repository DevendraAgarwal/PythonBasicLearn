# Dunder Method

class Tv:
    
    def __init__(self, name: str, price: float):
        # Constructor
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f'TV Object, name: str {self.name}, price: float {self.price}'
    
    def __str__(self):
        return f'TV {self.name} Price is {self.price}'
    
    def __add__(self, other):
        return f'{self.name} + {other.name} Price Was {self.price+other.price}'
    
    """ 
    __mul__
    __sub__
    """
    
sony = Tv("Sony Xperia", 59999.99)
samsung = Tv("Samsung", 39999.99)

print(sony.name)
print(sony.price)
print(repr(sony))
print(sony)

print(sony+samsung)

# Variable Dunder Methods

v = 4.5896
print(v.__ceil__())
print(v.__floor__())

""" 
Get All Dunder Methods

dir(<type>)
"""