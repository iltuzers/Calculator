from infix import Infix
from postfix import Postfix
import sys


def calculate(infix):
    """Returns the result of the calculation
    :param infix: A mathematical expression
    :type infix: str
    :rtype: float
    :return: Evaluation of the infix expression
    
    """

    postfix = Infix.infix_to_postfix(infix)
    return Postfix.evaluate(postfix)

def main():

    while True:

        try:
            infix_exp = input("Press Ctrl-C or (Ctrl-Z + Enter) to exit. Otherwise Calculate: ")
  
        except (EOFError, KeyboardInterrupt):
            print("Exiting")
            break

        try:
            result = calculate(infix_exp)

        except ValueError:
            pass

        else:
            print(infix_exp + " = " + str(result))
            

if __name__ == "__main__":
    main()



