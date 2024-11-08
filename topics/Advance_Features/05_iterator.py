# Iterator

# Method 1 By using iter Function
lst = [10,20,30,40,50]

it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Class Based Iterable Object
class Even:
    
    def __init__(self, len):
        self.len = len
        self.num = 0
        
    def __next__(self):
        if self.num < self.len:
            self.num = self.num+1
            return self.num
        else:
            raise StopIteration
        
    def __iter__(self):
        self.num = 0
        return self

for i in Even(100):
    print(i)