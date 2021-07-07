"""
@Author: Ranjith G C
@Date: 2021-07-07
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-07 
@Title : Program Aim is to validate user entered details using regular expression.
"""

from UserValidation import Validation as validate
import unittest

class TestUserValidation(unittest.TestCase):
    
    def test_givenValidFirstName_shouldReturnTrue(self):
        '''
        Description:
            The given valid first name should return true in this test case.
        '''

        self.assertTrue(validate.validateName("Ranjithgc"))
        self.assertTrue(validate.validateName("Abc"))

    def test_givenInvalidFirstName_shouldReturnFalse(self):
        '''
        Desription:
            The given invalid first name should return false in this test case.
        '''

        self.assertFalse(validate.validateName("Ra"))
        self.assertFalse(validate.validateName("ranjith"))
        self.assertFalse(validate.validateName("RANJITH"))
        self.assertFalse(validate.validateName("Ranj1th"))
        self.assertFalse(validate.validateName("R@njith"))
        
    def test_givenValidLastName_shouldReturnTrue(self):
        '''
        Description:
            The given valid last name should return true in this test case.
        '''

        self.assertTrue(validate.validateName("Arun"))
        self.assertTrue(validate.validateName("Aru"))
    
    def test_givenInValidLastName_shouldReturnFalse(self):
        '''
        Description:
            The given invalid last name should return false in this test case.
        '''

        self.assertFalse(validate.validateName("arun"))
        self.assertFalse(validate.validateName("Ar"))
        self.assertFalse(validate.validateName("ARN"))  
        self.assertFalse(validate.validateName("Ar1"))
        self.assertFalse(validate.validateName("@ru"))

    def test_givenValidEmail_shouldReturnTrue(self):
        '''
        Description:
            The given valid email should return true in test case
        Parameter:
            It takes self as a parameter.
        '''

        self.assertTrue(validate.validateEmail("abc10@yahoo.com"))
        self.assertTrue(validate.validateEmail("abc-100@yahoo.com"))

    def test_givenInvalidEmail_shouldReturnFalse(self):
        '''
        Description:
            The given invalid Email should return false in test case
        Parameter:
            It takes self as a parameter.
        '''

        self.assertFalse(validate.validateEmail("ranjith@.com"))
        self.assertFalse(validate.validateEmail("ran@gmail"))

    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            The given valid Phone number should return true in test case
        Parameter:
            It takes self as a parameter.
        """
        self.assertTrue(validate.validateNumber("+91-8618663565"))
        self.assertTrue(validate.validateNumber("+91 6865123321"))

    
    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
        Description:
            The given invalid phone number should return true in test case
        Parameter:
            It takes self as a parameter.
        """
        self.assertFalse(validate.validateNumber("+91-874543"))
        self.assertFalse(validate.validateNumber("+91-0432346578"))
        self.assertFalse(validate.validateNumber("+91 572781254324"))
        self.assertFalse(validate.validateNumber("7865438768"))
        self.assertFalse(validate.validateNumber("+91  6587654324"))
        self.assertFalse(validate.validateNumber("+91-876365r324"))
        self.assertFalse(validate.validateNumber("+91-87656@r324"))

    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            The given valid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertTrue(validate.validatePassword("arunranjith"))

    def test_givenInValidPassword_shouldReturnFalse(self):
        """
        Description:
            The given Invalid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertFalse(validate.validatePassword("arunranjith12"))
        self.assertFalse(validate.validatePassword("arunran"))

    def test_givenValidPassword_1UpperCase_shouldReturnTrue(self):
        """
        Description:
            The given valid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertTrue(validate.validatePassword("Arunranjith"))

    def test_givenInValidPassword_1UpperCase_shouldReturnTrue(self):
        """
        Description:
            The given valid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertFalse(validate.validatePassword("arunranjith"))

