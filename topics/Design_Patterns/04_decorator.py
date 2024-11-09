class Decorator:
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

class ConcreteComponent:
    def operation(self):
        print("Original operation")

class ConcreteDecorator1(Decorator):
    def operation(self):
        super().operation()
        print("Decorator 1 extension")

class ConcreteDecorator2(Decorator):
    def operation(self):
        super().operation()
        print("Decorator 2 extension")

# Usage:
component = ConcreteComponent()
decorator1 = ConcreteDecorator1(component)
decorator2 = ConcreteDecorator2(decorator1)

decorator2.operation()  # Output: Original operation, Decorator 1 extension, Decorator 2 extension