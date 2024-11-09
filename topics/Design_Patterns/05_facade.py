class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        self.subsystem1.operation1()
        self.subsystem2.operation2()

class Subsystem1:
    def operation1(self):
        print("Subsystem 1: Operation 1")

class Subsystem2:
    def operation2(self):
        print("Subsystem 2: Operation 2")

# Usage:
facade = Facade()
facade.operation()  # Output: Subsystem 1: Operation 1, Subsystem 2: Operation 2