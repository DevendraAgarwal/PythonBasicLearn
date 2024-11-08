from .inputHandler import inputHandler
from .calculatorSkeleton import calculatorSkeleton


class calculator(calculatorSkeleton,inputHandler):
    """My Calculator Class : Please Initialize calculator Class Object with ()"""    
    
    def square(self) -> float:
        """Get The Square of a Number

        Returns:
            float: Square of Base Number
        """
        self.methodWithDefinition()
        self.takeOneInput()
        return self.x**2
    
    def add(self) -> float:
        """Return the Sum of Two Numbers

        Returns:
            float: Sum of two Number
        """
        
        self.takeTwoInput()
        return self.x+self.y