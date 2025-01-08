# Клас для реалізації ЗПН
class Calculator:

    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

    # Метод для переведення виразу в ЗПН
    def to_rpn(self, expression):
        output = []
        operators = []
        tokens = self.tokenize(expression)

        for token in tokens:
            if token.isnumeric():  # Якщо токен - операнд, додаємо до виходу
                output.append(token)
            elif token == '(':  # Якщо токен - відкрита дужка, додаємо в стек
                operators.append(token)
            elif token == ')':  # Якщо токен - закрита дужка, виводимо оператори до '('
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Викидаємо '('
            else:  # Якщо токен - оператор, обробляємо стек
                while (operators and operators[-1] != '(' and
                       (self.precedence[token] < self.precedence[operators[-1]] or
                        (self.precedence[token] == self.precedence[operators[-1]] and
                         self.associativity[token] == 'L'))):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    # Метод для розбиття виразу на токени
    def tokenize(self, expression):
        tokens = []
        num = ''
        for char in expression:
            if char.isdigit() or char == '.':  # Якщо цифра або крапка (для чисел з плаваючою точкою)
                num += char
            else:
                if num:
                    tokens.append(num)
                    num = ''
                if char in self.precedence or char in '()':
                    tokens.append(char)
        if num:
            tokens.append(num)
        return tokens

    # Метод для обчислення результату ЗПН
    def evaluate_rpn(self, rpn):
        stack = []
        for token in rpn:
            if token.isnumeric():  # Якщо токен - операнд, додаємо до стеку
                stack.append(float(token))
            else:  # Якщо токен - оператор, виконуємо операцію
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
        return stack[0]  # Результат в кінці стеку

# Основна частина програми
if __name__ == "__main__":
    expression = input("Введіть математичний вираз: ")

    calc = Calculator()

    # Переведення виразу в ЗПН
    rpn = calc.to_rpn(expression)
    print(f"ЗПН: {' '.join(rpn)}")

    # Обчислення результату
    result = calc.evaluate_rpn(rpn)
    print(f"Результат: {result}")

