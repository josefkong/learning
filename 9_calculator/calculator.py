from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        calculation = operations[operation_symbol]
        num2 = float(input("What's the next number?: "))
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Type 'y' to continue calculating with {second_answer}, or type 'n' to exit. ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()