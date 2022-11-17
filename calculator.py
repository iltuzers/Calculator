import infix
import postfix
import sys

class Calculator:
    def __init__(self):
        self.calc = calc

    def calculate(infix):
        postfix = infix_to_postfix(infix)
        return evaluate_postfix(postfix)


def main():
    infix = input("Calculate: ")
    result = calculate(infix)
    print(infix + "= " + str(result))

    # Take a file as command line argument : First txt file
    # Scan the file and find all valid infix expressions
    # Evaluate them
    # 


if __name__ == "__main__":
    main()



