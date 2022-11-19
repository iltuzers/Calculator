from infix import Infix
from postfix import Postfix
import pytest


def test_parse_exp():
    assert Infix.parse_exp("4") == "4"
    assert Infix.parse_exp("4 - 3") == "4 - 3"
    assert Infix.parse_exp("4 -3") == "4 - 3"
    assert Infix.parse_exp("4-3") == "4 - 3"
    assert Infix.parse_exp("2.-") == "2. -"
    assert Infix.parse_exp(").") == ") ."
    assert Infix.parse_exp("30.23- 4.1* (3-4 ) /4-4") == "30.23 - 4.1 * ( 3 - 4 ) / 4 - 4"

def test_parse_error():
   
    with pytest.raises(ValueError):
        Infix.parse_exp("")
    with pytest.raises(ValueError):
        Infix.parse_exp("3a+")
    
def test_add_space():
    assert Infix.add_space("2.+") == "2. +"
    assert Infix.add_space("2.") == "2."
    assert Infix.add_space("()") == "( )"
    assert Infix.add_space("") ==""

def test_is_valid():
    assert Infix.is_valid("3") == True
    assert Infix.is_valid("( 7 + 8 )") == True
    assert Infix.is_valid("30.23 - 4.1 * ( 3 - 4 ) / 4 - 4") == True
    assert Infix.is_valid("( )") == False
    assert Infix.is_valid("2. -") == False
    assert Infix.is_valid("3. +") == False
    assert Infix.is_valid(") (") == False
    assert Infix.is_valid("") == False
    assert Infix.is_valid("*") == False


def test_infix_to_postfix():
    assert Infix.infix_to_postfix("2") == "2"  
    assert Infix.infix_to_postfix("30.23- 4.1* (3-4 ) /4-4") == "30.23 4.1 3 4 - * 4 / - 4 -"

def test_infix_to_postfix_error():
    with pytest.raises(ValueError):
        Infix.infix_to_postfix("")
    with pytest.raises(ValueError):
        Infix.infix_to_postfix("")
    with pytest.raises(ValueError):
        Infix.infix_to_postfix("(")
    with pytest.raises(ValueError):
        Infix.infix_to_postfix(")")
    with pytest.raises(ValueError):
        Infix.infix_to_postfix("+-*/()")
    with pytest.raises(ValueError):
        Infix.infix_to_postfix("()")



   

def test_evaluate_postfix():
    assert Postfix.evaluate("3 4 +") == 7
    assert Postfix.evaluate("1 2 12 4 - * 8 / - 3 -") == -4



