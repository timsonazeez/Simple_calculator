"""A simple calculator programme on addition, subtraction, divisin, multiplcation, remainder, power and square root."""

from math import sqrt

while True:
    print("(Enter 'q' to exit.)")
    
    First_Number = input("First Number: ")
    operator = input("operation ")
    if str(First_Number) == "q":
        break

    if operator == "sqrt":
        try:
            square_root = sqrt(int(First_Number))
        except ValueError:
            print("Cannot calculate the square root of negative.")
        print(square_root)

    else:

        Second_Number = input("Second Number: ")
        if str(Second_Number) == "q":
            break
        
        if operator == "+":
            try:
                sum = int(First_Number) + int(Second_Number)
            except ValueError:
                 print("A number is required not an alphabet.")
            print(sum)
            
        elif operator == "-":
            try:
                sub = int(First_Number) - int(Second_Number)
            except ValueError:
                print("A number is required not an alphabet.")
            else:
                print(sub)
        
        elif operator == "*":
            try:
                Multi = int(First_Number) * int(Second_Number)
            except ValueError:
                print("A number is required not an alphabet.")
            else:
                print(Multi)
        
        elif operator == "%":
            try:
                modu = int(First_Number) % int(Second_Number)
            except ValueError:
                print("A number is required not an alphabet")
            except ZeroDivisionError:
                print("You can't divide by zero.")
            else:
                print(modu)
        
        elif operator == "**":
                try:
                    power = int(First_Number) ** int(Second_Number)
                except ValueError:
                    print("A number is required not an alphabet")
                except ZeroDivisionError:
                    print("You can't have zero raise to power of negative value.")
                else:
                    print(power)
            
        elif operator == "/":
                try:
                    Division = round(int(First_Number) / int(Second_Number), 4) # The division is meant to round up value to four decimal places
                except ZeroDivisionError:
                    print("You can't divide by zero.")
                except ValueError:
                    print("A number is required not an alphabet.")
                else:
                    print(Division)
            
    
