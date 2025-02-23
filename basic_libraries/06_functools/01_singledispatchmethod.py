from functools import singledispatchmethod

class Cooking:

    @singledispatchmethod
    def cook(self, arg):
        return f"I'm cooking {arg} eggs."

    @cook.register
    def _(self, arg: int):
        return f"I'm cooking exactly {arg} eggs."

    @cook.register
    def _(self, arg: bool):
        return f"Am I cooking eggs? {arg}"
    
    @cook.register
    def _(self, arg: int, type: str):   # type is an additional argument
        # This Will be called when the first argument is an integer
        return f"I'm cooking {arg} {type} eggs."
    
cake = Cooking()
print(cake.cook("scrambled"))   # I'm cooking scrambled eggs.
print(cake.cook(5))             # I'm cooking exactly 5 eggs.
print(cake.cook(True))          # Am I cooking eggs? True
# print(cake.cook(3, "fried"))    # Raise Error
