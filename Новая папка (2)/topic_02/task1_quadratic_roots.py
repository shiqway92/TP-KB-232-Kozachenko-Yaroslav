
from Tema1_Functions_and_Variables.task3_discriminant import calculate_discriminant

def find_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        return -b / (2 * a),
    else:
        return None

if __name__ == "__main__":
    a, b, c = 1, -3, 2
    print(f"Roots of {a}x^2 + {b}x + {c} = 0: {find_roots(a, b, c)}")
