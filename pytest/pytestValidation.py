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

@pytest.mark.email
@pytest.mark.parametrize("valid_email,expected",input.valid_email)

def test_validEmail(valid_email,expected):
    """
    Description:
        The given valid email should return true in test case
    Parameter:
        It takes valid_email and expected as a parameter.   
    """

    assert validate.validateEmail(valid_email) == expected

@pytest.mark.email
@pytest.mark.parametrize("invalid_email,expected",input.inValid_email)

def test_invalidEmail(invalid_email,expected):
    """
    Description:
        The given invalid Email should return false in test case
    Parameter:
        It takes invalid_email_input and expected as parameter.
    """

    assert validate.validateEmail(invalid_email) == expected

@pytest.mark.phonenumber
@pytest.mark.parametrize("phone_number, expected", input.valid_number)
def test_validPhoneNumber(phone_number,expected):
    """
    Description:
        The given valid Phone number should return true in test case
    Parameter:
        It takes phone_number_ input and expected as a parameter.
    """

    assert validate.validateNumber(phone_number) == expected

@pytest.mark.phonenumber
@pytest.mark.parametrize("invalid_number, expected",input.inValid_number)
def test_invalidPhoneNumber(invalid_number,expected):
    """
    Description:
        The given invalid phone number should return false in test case
    Parameter:
        It takes invalid_phone number and expected as a parameter
    """

    assert validate.validateNumber(invalid_number) == expected

@pytest.mark.password
@pytest.mark.parametrize("valid_password, expected",input.valid_password)

def test_validPassword(valid_password,expected):
    """
    Description:
        The given valid Password should return true in test case
    Parameter:
        It takes valid_password and expected as a parameter
    """

    assert validate.validatePassword(valid_password) == expected
    
@pytest.mark.password
@pytest.mark.parametrize("invalid_password, expected",input.inValid_password)

def test_invalidPassword(invalid_password,expected):
    """
    Description:
        The given invalid Password should return false in test case
    Parameter:
        It takes invalid_password and expected as a parameter
    """

    assert validate.validatePassword(invalid_password) == expected



