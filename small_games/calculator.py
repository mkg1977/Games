
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

opperations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for key in opperations:
        print(key)

    should_continue = True
    while should_continue:
        symbol = input("Pick up an opperation from the line above: ")
        num2 = float(input("Wht's the second number?: "))
        calculation = opperations[symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"(Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' for exit from the program: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
    





