from calculator_art import logo

operators = ['+', '-', '*', '/']


def operate(op, a, b):
    match op:
        case 0:
            return a + b
        case 1:
            return a - b
        case 2:
            return a * b
        case 3:
            return a / b


def calculator():
    print(logo)
    running = True
    first_operand = float(input("What's the first number?\n"))

    for operator in operators:
        print(f"{operator}")

    while running:
        operator = input("Pick an operator:\n")
        second_operand = float(input("What's the second number?\n"))
        # .index() throws an error if an invalid operator was entered
        result = operate(operators.index(operator), first_operand, second_operand)
        print(f"{first_operand} {operator} {second_operand} = {result}")
        # anything but 'y'/'r' terminates
        command = input(f"Type 'c' to continue calculating with {result}, or type 'r' to start a new calculation. Type 't' to terminate.\n")
        if command == 'c':
            first_operand = result
        elif command == 'r':
            calculator()
        else:
            running = False

    print("Terminating")
    return


calculator()
