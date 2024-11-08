from calculator.myCalculator import calculator
from calculator.outputHandler import outputHandler as oph
from calculator.inputHandler import inputHandler as iph

""" 
Create Object With () For Implementing ans Work the Interface Properly
Without () Interface are not working
"""
calc = calculator()

def printResult(result: float):
    result = str(result)
    # Print The Output by Using 2 Ways
    print('\n----------------------------------------------------------')
    oph.greenMessage("FORMATTED STRING: Your Squared Number is : "+result)
    print('\033[1;92;40mWITHOUT FORMATTED: Your Squared Number is :',result,'\033[0m')
    print('------------------------------------------------------------')
    
def calculatorOperationCaller(operation: int):
    # Call the Above Defined Function From Calculator Class Based On Operation Selected By User
    if operation == 1:
        printResult(calc.square())
        
    elif operation == 2:
        printResult(calc.add())
        
    else:
        oph.redMessage("Please Choose Valid Operation. Please Try Again..")

while(True):
    
    # Print All the Available Operations
    print('''\nOperations:
    1. Square
    2. Add
    9. Exit
    \nChoose Corresponding Number''')

    try:
        # Taking Operation Input From User
        operation = iph.getSingleInputInInteger(
            iph,
            "Enter What Operation you want to perform:"
        )
    except ValueError:
        oph.redMessage("Please Choose Valid Operation. Please Try Again...")
        continue
    
    if operation == 9:
        oph.greenMessage("... Thankyou For Using Calculator ... Bye Bye")
        break
    else:
        try:
            calculatorOperationCaller(operation=operation)
        except TypeError:
            continue
        except ValueError:
            continue