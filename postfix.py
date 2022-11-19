from Stack import Stack
from Queue import Queue

class Postfix:

    postfix_expression = ""
  
    @staticmethod
    def evaluate(postfix_exp):
        """ Evaluates postfix expression and returns it
        :param postfix_exp: A postfix expression
        :type postfix_exp: str
        :rtype: float
        :return: evaluation of postfix_exp
        
        """
         
        operand_stack = Stack()
        result = 0
        for symbol in postfix_exp.split():
            if Postfix.is_number(symbol):
                operand_stack.push(symbol)
            elif symbol in "+-/*":
                second_op, first_op = float(operand_stack.pop()), float(operand_stack.pop()) # Top of the stack is the last element
                result = Postfix.apply_operator(first_op, second_op, symbol)
                operand_stack.push(result)

            else:
                raise ValueError("Postfix is not a valid expression")
        result = operand_stack.pop() 
        return result

    @staticmethod  
    def apply_operator(num1, num2, operator):
        """Returns the result of the mathematical expression
        :param num1: First number
        :param num2: Second number
        :param operator: A mathematical operator
        :type num1: float
        :type num2: float
        :type operator: string
        :rtype: float
        :return: evaluation of operator being applied to the numbers num1 and num2
        """
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

    # Checks if a string is a float or int
    @staticmethod
    def is_number(anumber):
        """ Returns True if anumber is float or int, False otherwise
        :param anumber: Number
        :type anumber: str
        :rtype: bool
        :return: True or False
        """
        for i in anumber:
            if not (i.isdigit() or i == "."):
                return False
        if anumber.endswith("."):
            return False
        return True
