
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print(f"Result: {divide(a, b)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        if input("Continue? (y/n): ").lower() != 'y':
            break
