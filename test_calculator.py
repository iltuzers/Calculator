from calculator import infix_to_postfix, evaluate_postfix, parse_exp


def test_infix_to_postfix():
    assert infix_to_postfix("") == ""
    assert infix_to_postfix("3 + 4") == "3+4"
    assert infix_to_postfix("3+4") == "3+4"
    assert infix_to_postfix("2 + 5*3-(10 /2)*3+2") == "253*+102*"

def test_evaluate_postfix():
    ...

def test_parse_exp():
    ...

def test_add_space():
    ...