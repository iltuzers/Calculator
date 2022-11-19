from Stack import Stack
from Queue import Queue
from postfix import Postfix
import sys

class Infix:
    """
    A class that defines methods that tries to convert a string to the infix form and eventually to the postfix form

    Attributes:
    --------------
    infix_expression : str
                String to be converted to a valid infix form with spaces

    Methods:
    ---------------
    parse_exp(expression) : Parses input and removes all spaces so that the algorithm works with strings with improper spaces
    add_space(expression): Add spaces properly
    is_valid(expression) :  True if an expression is in proper input form, False otherwise
    is_valid_no_par(Queue()) : This method checks if an expression without paranthesis is a proper input expression
    infix_to_postfix(expression) : It converts an infix expression to a postfix expression 
    """

    infix_expression = ""
    
    # Accepts inputs with or without spaces
    @staticmethod
    def parse_exp(exp):
        """ Returns an input expression with spaces

        :param exp: a possible infix expression
        :type exp: str
        :rtype: str
        :return: exp with spaces between operators, numbers, and paranthesis
        """
        
        for s in exp:
            if s not in "0123456789. +-*/()": # Permitted characters, otherwise it's not a proper infix expression
                raise ValueError("Invalid Character")
        
        if exp != "": 
            infix_exp = "".join(exp.split()) # Remove white spaces so that we can add it between all items properly
            spaced_exp = Infix.add_space(infix_exp)
        else:
            raise ValueError("Empty string")
        return spaced_exp
    
    # Input: infix without spaces, Output: Infix with spaces
    @staticmethod
    def add_space(exp):
        """ Returns an infix expression with proper spaces
        :param exp: infix expression without space
        :type exp: str
        :rtype: str
        :return: exp with spaces
        """
        number_queue = Queue() # This is needed to accommodate decimal and multidigit numbers.
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
    
    # Assumes infix_expression has spaces between items
    @staticmethod
    def is_valid(exp):
        """ Returns True if exp is an infix expression, False otherwise
        :param exp: an expression
        :type exp: str
        :rtype: bool
        :return: True or False
        """
        par_stack = Stack() # checks if parantheses match
        queues = [] # Create new queue for each paranthesis
        for item in exp.split():
            if item == "(":
                par_stack.push(item) # Add ( for each paranthesis
                queues.append(Queue()) # Create a queue for the terms in that paranthesis
                
            elif item == ")":
                if par_stack.is_empty(): 
                    return False  # ) can not come before (
                else:
                    par_stack.pop()
                    if Infix.isvalid_no_par(queues.pop()): # If there is a valid infix expression inside the last paranthesis, replace it an arbitrary number
                        # Add an arbitrary number to the last queue.
                        if len(queues) == 0:
                            queues.append(Queue()) # Removed the last queue above
                        queues[len(queues) - 1].enqueue('5') #Here, replacing (infix_expression) by 5. It won't change the validity of the infix exp
                    else:
                        return False
            else:
                if len(queues) == 0:
                    queues.append(Queue())
                queues[len(queues) - 1].enqueue(item)
        if len(queues) != 1:
            return False # ""
        else:
            # There should be one queue left in the end, we kept replacing (infix) by 5
            return Infix.isvalid_no_par(queues.pop()) 
    
    # There is no paranthesis. It should be in the form of : num op num op num..
    @staticmethod
    def isvalid_no_par(queue):
        """ Returns True if items of Queue() forms an infix expression, False otherwise.
            Queue doesn't have paranthesis.
            It's infix if it's in this form -> number operator number operator number ...
        :param queue: a Queue() object that contains numbers and operators
        :type queue: Queue class
        :rtype: bool
        :return: True or False
        """
        counter = 0
        if queue.is_empty():
            return False

        while not queue.is_empty():
            next_item = queue.dequeue()
            
            
            if str(next_item) in "/*+-":
                if counter % 2 == 0: # Odd indices have to be operators
                    return False
            elif Postfix.is_number(next_item):
                if counter % 2 == 1: # Even indices have to be numbers
                    return False
            else:
                # next item is not a valid number. Like, 2.
                return False
            counter += 1
        
        return True
    
 
    """ Returns Postfix Expression with spaces"""
    @staticmethod
    def infix_to_postfix(exp):
        """ Returns postfix expression corresponding to the infix expression exp
        :param exp: infix expression
        :type exp: str
        :rtype: str
        :return: postfix expression
        
        """
        infix = Infix.parse_exp(exp)
        postfix_list = []
        operator_stack = Stack()
        prec = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0} # Need it to compare precedence of Stack symbols
        if Infix.is_valid(infix):
            for symbol in infix.split():
                if symbol == "(":
                    operator_stack.push(symbol)
                elif symbol in "+-*/":

                    if not operator_stack.is_empty():
                        while not operator_stack.is_empty() and prec[symbol] <= prec[operator_stack.peek()]:
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
        else:
            raise ValueError("Invalid infix")
            
        return " ".join(postfix_list)
    


