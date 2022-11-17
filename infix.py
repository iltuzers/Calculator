from Stack import Stack
from Queue import Queue
from postfix import Postfix
import sys

class Infix:

    def __init__(self, exp=""):
        self.infix_expression = exp

    @property
    def infix_expression(self):
        return self._infix_expression
    
    @infix_expression.setter
    def infix_expression(self, infix):
        self._infix_expression = infix
    
        # Accepts inputs with or without spaces
    def parse_exp(self, exp):
            for s in exp:
                if s not in "0123456789. +-*/()":
                    raise ValueError("Invalid Character")
            infix_exp = "".join(exp.split()) # Remove white spaces
            spaced_exp = self.add_space(infix_exp)
            return spaced_exp
    
    # Input: infix without spaces, Output: Infix with spaces
    def add_space(self):
        number_queue = Queue()
        spaced_exp = ""
        for i in self.expression:
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
    
     # Assumes infix_expression has spaces between items
    def is_valid(self):
        paran_stack = Stack() # checks if parantheses match
        queues = [] # Create new queue for each paranthesis
        for item in self.infix_expression.split():
            if item == "(":
                paran_stack.push(item)
                queues.append(Queue())
                
            elif item == ")":
                if paran_stack.is_empty():
                    return False
                else:
                    paran_stack.pop()
                    if Infix.is_infix(queues.pop()): # If there is a valid infix expression inside the last paranthesis, replace it an arbitrary number
                        queues[len(queues) - 1].enqueue(5) # Add an arbitrary number to the last queue
                    else:
                        return False
            else:
                queues[len(queues) - 1].enqueue(item)
        if len(queues) != 1:
            print("Something is wrong")
        else:
            return Infix.is_infix(queues.pop())
    
    # There is no paranthesis. It should be in the form of : num op num op num..
    @staticmethod
    def is_infix(queue):
        counter = 0
        while not queue.is_empty():
            
            if Infix.is_number(queue.dequeue()):
                if counter % 2 == 1: # Even indices have to be numbers
                    return False
            elif queue.dequeue() in "/*+-":
                if counter % 2 == 0: # Odd indices have to be operators
                    return False
            counter += 1
        return True
    
    # Checks if a string is a float or int
    @staticmethod
    def is_number(anumber):
        for i in anumber:
            if not (i.isdigit() or i == "."):
                return False
        return True

    """ Returns Postfix Expression with spaces"""
    def infix_to_postfix(self):
        infix = self.parse_exp()
        postfix_list = []
        operator_stack = Stack()
        prec = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0} # Need it to compare precedence of Stack symbols
        for symbol in infix.split():
            if symbol == "(":
                operator_stack.push(symbol)
            elif symbol in "+-*/":

                if not operator_stack.is_empty():
                    while prec[symbol] <= prec[operator_stack.peek()] and not operator_stack.is_empty():
                        postfix_list.append(operator_stack.pop())
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
        
        
        return Postfix(" ".join(postfix_list))





    
    
        
    
