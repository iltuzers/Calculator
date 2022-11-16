from calculator import infix_to_postfix, evaluate_postfix, parse_exp, add_space


def test_infix_to_postfix():
    assert infix_to_postfix("") == ""
    assert infix_to_postfix("3 + 4") == "3 4 +"
    assert infix_to_postfix("3+4") == "3 4 +"
    #assert infix_to_postfix("30.23- 4.1* (3-4 ) /4-4") == "30.23 4.1 3 4 - * 4 / - 4 -"
    #assert infix_to_postfix("1- 2* (3-4 ) /5-6") == "1 2 3 4 - * 5 / - 6 -"
    


   

def test_evaluate_postfix():
    assert evaluate_postfix("") == 0
    assert evaluate_postfix("3 4 +") == 7
    


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
