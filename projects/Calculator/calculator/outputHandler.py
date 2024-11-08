

class outputHandler:
    """Output Handling Function for Terminal
    """
    
    def greenMessage(message: str):
        print(f"\033[1;92;40m{message}\033[0m")
        
    def redMessage(message: str):
        print(f"\033[1;31;40m{message}\033[0m")
        
    def greyMessage(message: str):
        print(f"\033[1;30;40m{message}\033[0m")