from Stack import Stack

def infix_to_postfix(infix_exp):
    ...

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



