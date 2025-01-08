
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

def calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        if operation == "exit":
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operation == "+":
                print(f"Result: {add(a, b)}")
            elif operation == "-":
                print(f"Result: {subtract(a, b)}")
            elif operation == "*":
                print(f"Result: {multiply(a, b)}")
            elif operation == "/":
                print(f"Result: {divide(a, b)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
