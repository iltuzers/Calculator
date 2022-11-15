from Stack import Stack
import sys


"""
Algorithm:
1. If (
2. If ), then pop the stack until (
3. If 0..9, then add it to the list


"""
def infix_to_postfix(infix_exp):
    infix = parse_exp(infix_exp)
    postfix_list = []
    operator_stack = Stack()
    prec = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0} # Need it to compare precedence of Stack symbols

    for i in infix:
        if i in "(/*+-":
            if not operator_stack.is_empty():
                top = operator_stack.peek()
                while prec[i] <= prec[top]:
                    top = operator_stack.pop()
                    postfix_list.append(top)
            operator_stack.push(i)

        elif i == ")":
            try:
                top = operator_stack.pop()
                while top != "(":
                    postfix_list.append(top)
                    top = operator_stack.pop()
            except IndexError:
                sys.exit("Not a valid expression")
            
        else:
            postfix_list.append(i)
    
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    
    return "".join(postfix_list)





def evaluate_postfix(postfix_exp):
    ...

def parse_exp(exp):
        for s in exp:
            if s not in "0123456789 +-*/()":
                raise ValueError("Invalid Character")
        exp_list = str(exp.split())
        return exp_list

def main():
    infix = input("Calculate: ")
    postfix = infix_to_postfix(infix)
    result = evaluate_postfix(postfix)
    print(infix + "= " + str(result))


if __name__ == "__main__":
    main()



