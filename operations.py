import random
import time

class MathGame:


    def generate_expression(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        self.expression = f"{num1} {operator} {num2}"
        return self.expression.strip()

    def solve_expression(self):
        self.result = eval(self.expression)
        return str(self.result).strip()

    def set_new_expression(self):
        self.generate_expression()
        self.solve_expression()