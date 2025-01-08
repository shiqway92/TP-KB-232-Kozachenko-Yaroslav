from operations import add, subtract, multiply, divide

class Calculator:
    def calculate(self, operation, a, b):
        if operation == "add":
            return add(a, b)
        elif operation == "subtract":
            return subtract(a, b)
        elif operation == "multiply":
            return multiply(a, b)
        elif operation == "divide":
            return divide(a, b)
        else:
            raise ValueError("Invalid operation.")

if __name__ == "__main__":
    calc = Calculator()
    print(calc.calculate("add", 10, 5))       # 15
    print(calc.calculate("subtract", 10, 5))  # 5
    print(calc.calculate("multiply", 10, 5))  # 50
    print(calc.calculate("divide", 10, 5))    # 2
