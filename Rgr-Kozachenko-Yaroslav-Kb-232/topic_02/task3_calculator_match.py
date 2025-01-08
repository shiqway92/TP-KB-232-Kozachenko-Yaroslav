
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
            match operation:
                case "+":
                    print(f"Result: {add(a, b)}")
                case "-":
                    print(f"Result: {subtract(a, b)}")
                case "*":
                    print(f"Result: {multiply(a, b)}")
                case "/":
                    print(f"Result: {divide(a, b)}")
                case _:
                    print("Invalid operation.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
