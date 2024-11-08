from abc import ABC, abstractmethod

class calculatorSkeleton(ABC):
    """This Class is a Interface for calculator Class
    Please Initialize calculator Class Object with ()
    """
    
    @abstractmethod
    def square(self) -> float:
        pass
    
    @abstractmethod
    def add(self) -> float:
        pass
    
    def methodWithDefinition(self):
        print("Message From Method With Definition of Abstract Class")