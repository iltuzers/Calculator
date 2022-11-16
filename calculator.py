from Stack import Stack
from Queue import Queue
import sys
"""
TODO:
    check what happens if a number is decimal or if it is more than 1 digit
    I think I can use Queue to decimal numbers, 2 or more digit numbers
    or I should just place spaces between numbers

"""

"""
Algorithm:
1. If (
2. If ), then pop the stack until (
3. If 0..9, then add it to the list



"""
# assert '1 2 3 4 - * - 5 / 6 -' == '1 2 3 4 - * 5 / - 6 -'
""" Returns Postfix Expression with spaces"""
def infix_to_postfix(infix_exp):
    infix = parse_exp(infix_exp)
    postfix_list = []
    operator_stack = Stack()
    prec = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0} # Need it to compare precedence of Stack symbols
    for symbol in infix.split():
        if symbol in "(/*+-":
            if symbol == "(":
                operator_stack.push(symbol)
            elif symbol in "+-*/":

                if not operator_stack.is_empty():
                    top = operator_stack.pop()
                    while prec[symbol] <= prec[top] and not operator_stack.is_empty():
                        postfix_list.append(top)
                        top = operator_stack.pop()
                    
                operator_stack.push(symbol)

        elif symbol == ")":
            try:
                top = operator_stack.pop()
                while top != "(":
                    postfix_list.append(top)
                    top = operator_stack.pop()
            except IndexError:
                sys.exit("Infix is not a valid expression")
            
        else:
            postfix_list.append(symbol)
    
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    
    
    return " ".join(postfix_list)

def evaluate_postfix(postfix_exp):
    operand_stack = Stack()
    result = 0
    for symbol in postfix_exp.split():
        if is_number(symbol):
            operand_stack.push(symbol)
        elif symbol in "+-/*":
            second_op, first_op = int(operand_stack.pop()), int(operand_stack.pop()) # Top of the stack is the last element
            result = apply_operator(first_op, second_op, symbol)
            operand_stack.push(result)

        else:
            raise ValueError("Postfix is not a valid expression")
    return result

# Checks if a string is a float or int
def is_number(anumber):
    for i in anumber:
        if not (i.isdigit() or i == "."):
            return False
    return True

def calculate(infix):
    postfix = infix_to_postfix(infix)
    return evaluate_postfix(postfix)

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

# Accepts inputs with or without spaces
def parse_exp(exp):
        for s in exp:
            if s not in "0123456789. +-*/()":
                raise ValueError("Invalid Character")
        exp = "".join(exp.split()) # Remove white spaces
        exp = add_space(exp) 
        return exp

# Input: infix without spaces, Output: Infix with spaces
def add_space(exp):
    number_queue = Queue()
    spaced_exp = ""
    for i in exp:
        if i in "()+-*/":
            while not number_queue.is_empty():
                spaced_exp += number_queue.dequeue()
            spaced_exp += " " + i
        elif i in "0123456789.":
            if number_queue.is_empty(): # Need space before the number
                spaced_exp += " "
            number_queue.enqueue(i)
        
    if not number_queue.is_empty():
        while not number_queue.is_empty():
            spaced_exp += number_queue.dequeue()
    return spaced_exp.strip()

def main():
    infix = input("Calculate: ")
    result = calculate(infix)
    print(infix + "= " + str(result))


if __name__ == "__main__":
    main()



