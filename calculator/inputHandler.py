from .outputHandler import outputHandler


def printError():
    # Handling ValueError
    outputHandler.redMessage("Please Enter a Valid Number. Please Try Again...")

class inputHandler:
    x = None
    y = None
    
    def takeTwoInput(self):
        self.resetValues()
        try:
            self.x = float(self.greyInput("Enter First Number: "))
            self.y = float(self.greyInput("Enter Second Number: "))
        except ValueError:
            printError()
        
    def takeOneInput(self):
        self.resetValues()
        try:
            self.x = float(self.greyInput("Enter Your Number: "))
        except ValueError:
            printError()
            
    def resetValues(self):
        self.x = None
        self.y = None
        
    def getSingleInputInInteger(self, message: str):
        return int(self.greyInput(self,message))
    
    def greyInput(self, message: str):
        return input(f"\033[1;30;40m{message}\033[0m")