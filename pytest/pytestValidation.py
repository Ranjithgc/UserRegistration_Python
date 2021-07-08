"""
@Author: Ranjith G C
@Date: 2021-07-08
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-08 
@Title : Program Aim is to validate user entered details using regular expression.
"""
from UserValidation import UserValidation as validate
from Input import Sample as input

import pytest

@pytest.mark.name
@pytest.mark.parametrize("name_input,expected", input.valid_name)
def test_validName(name_input,expected):
    """
    Description:
        The given valid name should return true in test case
    Parameter:
        It takes name_input and expected as a parameter.
    """
    
    assert validate.validateName(name_input) == expected

@pytest.mark.name
@pytest.mark.parametrize("invalid_name,expected",input.invalid_name)

def test_invalidName(invalid_name, expected):
    """
    Description:
        The given invalid name should return false in test case
    Parameter:
        It takes invalid_name and expected as a parameter..
    """

    assert validate.validateName(invalid_name) == expected


