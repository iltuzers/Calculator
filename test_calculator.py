from infix import infix_to_postfix, parse_exp, add_space, is_valid
from postfix import evaluate_postfix

def test_infix_to_postfix():
    assert infix_to_postfix("") == ""
    assert infix_to_postfix("3 + 4") == "3 4 +"
    assert infix_to_postfix("3+4") == "3 4 +"
    assert infix_to_postfix("()") == ""
    #assert infix_to_postfix("(") == "" # Not a valid expression. Probably need to use regex.
    #assert infix_to_postfix(")") == ""
    #assert infix_to_postfix("+-*/()") == "* / + -" # This doesn't make sense. Change it to "" later
    assert infix_to_postfix("30.23- 4.1* (3-4 ) /4-4") == "30.23 4.1 3 4 - * 4 / - 4 -"
    """ So far, we only checked if those characters exist. We need to check if input is a valid infix expression"""
   
#1-2(12-4)/8-3
def test_evaluate_postfix():
    assert evaluate_postfix("") == 0
    assert evaluate_postfix("3 4 +") == 7
    assert evaluate_postfix("1 2 12 4 - * 8 / - 3 -") == -4
    


def test_parse_exp():
    assert parse_exp("") == ""
    assert parse_exp(" ") == ""
    assert parse_exp("3+5") == "3 + 5"
    assert parse_exp("3+ 5") == "3 + 5"
    assert parse_exp("3+ 5") == "3 + 5"
    assert parse_exp("30.23- 4.1* (3-4 ) /4-4") == "30.23 - 4.1 * ( 3 - 4 ) / 4 - 4"

def test_add_space():
    assert add_space("") == ""
    assert add_space(" ") == ""
    assert add_space("3+5") == "3 + 5"
    assert add_space("2+3*(5-2)") == "2 + 3 * ( 5 - 2 )"
    assert add_space("30.23-4.1*(3-4)/4-4") == "30.23 - 4.1 * ( 3 - 4 ) / 4 - 4"
