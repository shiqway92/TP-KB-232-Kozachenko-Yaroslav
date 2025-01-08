
def calculate_discriminant(a, b, c):
    return b**2 - 4 * a * c

if __name__ == "__main__":
    a, b, c = 1, -3, 2
    print(f"Discriminant of {a}x^2 + {b}x + {c} = 0 is {calculate_discriminant(a, b, c)}")
