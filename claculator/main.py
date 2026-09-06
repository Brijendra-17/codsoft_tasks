class OperatorIsNotListed(Exception):  # Defines a custom exception for invalid operator input
    pass  # Ends the custom exception class


def operation(a,b):  # Defines the main arithmetic operation function
        try:  # Starts error handling for invalid operator input
            def cal():  # Defines a nested function to select the operation
                o = input("Enter the operation:")  # Takes the operator input from the user
                match o:  # Matches the input operator with supported cases
                        case "+":  # Handles addition
                            print(f"The Addition is: {a+b}")  # Prints the addition result
                        case "-":  # Handles subtraction
                            print(f"The Subtraction is: {a-b}")  # Prints the subtraction result
                        case "*":  # Handles multiplication
                            print(f"The Multiplication is: {a*b}")  # Prints the multiplication result
                        case "/":  # Handles division
                            print(f"The Division is: {a/b}")  # Prints the division result
                        case _:  # Handles any unsupported operator
                            print("Try Again")  # Warns the user to try again
                            raise OperatorIsNotListed("Enter listed operator only")  # Raises a custom exception for invalid operators
            cal()  # Calls the nested calculation function
        except OperatorIsNotListed as e:  # Catches invalid operator exceptions
            print("Enter Only Listed Operation")  # Displays an error message for invalid input
            def operation_should_correct():  # Defines a retry function for invalid operators
                try:  # Starts a retry block
                    cal()  # Calls the calculation function again
                except OperatorIsNotListed:  # Catches invalid operator again during retry
                    print("Enter Only Listed Operation")  # Prints the same validation message
                    operation_should_correct()  # Recursively retries until valid input is entered
            operation_should_correct()  # Runs the retry function



flag = "Y"
while flag == "Y" or flag == "y":
    try:  # Starts the main input block for numbers and operation
        a = float(input("enter The First Number:"))  # Reads and converts the first number
        b = float(input("enter The Second Number:"))  # Reads and converts the second number
        print("Enter the below operation to continue:\nFor Addition press +\nFor Subtraction press -\nFor Multiplication press *\nFor Division press /")  # Shows the available operations
        operation(a, b)  # Calls the operation function with the entered numbers
    except ZeroDivisionError as e:  # Catches division-by-zero errors
        print("Zero can not divide any number")  # Prints division-by-zero warning
        print("try any other Number")  # Suggests using another number

        def b_can_not_be_zero():  # Defines a retry function for invalid zero divisor input
            try:  # Starts the zero-check recovery block
                b = float(input("enter The Second Number:"))  # Reads the second number again
                operation(a, b)  # Re-runs the operation with the new value
            except ZeroDivisionError:  # Handles repeated division-by-zero case
                print("Zero can not divide any number")  # Prints error message again
                print("try any other Number")  # Requests a different input
                b_can_not_be_zero()  # Recursively retries until valid input is entered
            except ValueError:  # Handles non-numeric second input
                value_should_num()  # Calls the general value-retry function

        b_can_not_be_zero()  # Executes the zero-divisor correction function
    except ValueError as e_1:  # Catches invalid numeric input during initial number entry
        print("Value Should Be Numeric")  # Prints a numeric input error message

        def value_should_num():  # Defines a function to re-enter valid numeric values
            try:  # Starts the numeric validation retry block
                a = float(input("enter The First Number:"))  # Reads the first number again
                b = float(input("enter The Second Number:"))  # Reads the second number again
                print("Enter the below operation to continue:\nFor Addition press +\nFor Subtraction press -\nFor Multiplication press *\nFor Division press /")  # Shows operation menu again
                operation(a, b)  # Calls the operation function with corrected numbers
            except ValueError:  # Handles invalid numeric retry input
                print("Value Should Be Numeric")  # Prints the same validation message
                value_should_num()  # Recursively retries numeric input
            except ZeroDivisionError:  # Handles division-by-zero during retry
                b_can_not_be_zero()  # Calls the zero-divisor recovery function

        value_should_num()  # Starts the numeric correction process
    flag = input("press Y to continue And N for Exit : ")

     
            
        
         
    

            
