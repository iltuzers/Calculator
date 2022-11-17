from infix import Infix
from Stack import Stack
from Queue import Queue

class Postfix:
    def __init__(self, postfix_exp):
        self.postfix_expression = postfix_exp
    
    @property
    def postfix_expression(self):
        return self._postfix_expression
    
    @postfix_expression.setter
    def postfix_expression(self, postfix_exp):
        self._postfix_expression = postfix_exp

    def evaluate(self):
        operand_stack = Stack()
        result = 0
        for symbol in self.postfix_expression.split():
            if Infix.is_number(symbol):
                operand_stack.push(symbol)
            elif symbol in "+-/*":
                second_op, first_op = int(operand_stack.pop()), int(operand_stack.pop()) # Top of the stack is the last element
                result = Postfix.apply_operator(first_op, second_op, symbol)
                operand_stack.push(result)

            else:
                raise ValueError("Postfix is not a valid expression")
        return result

    @staticmethod  
    def apply_operator(num1, num2, operator):
        if operator == "/":
            return num1 / num2
        elif operator == "*":
            return num1 * num2
        elif operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        else:
            raise ValueError("Invalid operator")

