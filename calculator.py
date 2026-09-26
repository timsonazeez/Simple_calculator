"""A simple calculator programme on addition, subtraction, divisin and multiplcation."""

while True:
    print("(Enter 'q' to exit.)")
    
    First_Number = input("First Number: ")
    if str(First_Number) == "q":
        break

    operation = input("operation ")

    Second_Number = input("Second Number: ")
    if str(Second_Number) == "q":
        break

    if operation == "+":
        try:
            sum = int(First_Number) + int(Second_Number)
        except ValueError:
            print("A number is required not an alphabet.")
        print(sum)
    
    elif operation == "-":
        try:
            sub = int(First_Number) - int(Second_Number)
        except ValueError:
            print("A number is required not an alphabet.")
        else:
            print(sub)

    elif operation == "*":
        try:
            Multi = int(First_Number) * int(Second_Number)
        except ValueError:
            print("A number is required not an alphabet.")
        else:
            print(Multi)

    elif operation == "/":
        try:
            Division = int(First_Number) / int(Second_Number)
        except ZeroDivisionError:
            print("You can't divide by zero.")
        except ValueError:
            print("A number is required not an alphabet.")
        else:
            print(Division)
