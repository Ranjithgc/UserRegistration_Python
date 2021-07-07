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

        self.assertTrue(validate.validateEmail("ranjith10@yahoo.com"))
        self.assertTrue(validate.validateEmail("ranjith-100@yahoo.com"))
        self.assertTrue(validate.validateEmail("ran.100@yahoo.com"))
        self.assertTrue(validate.validateEmail("arun111@abc.com"))
        self.assertTrue(validate.validateEmail("arun-100@abc.net"))
        self.assertTrue(validate.validateEmail("arunra.100@abc.com.au"))
        self.assertTrue(validate.validateEmail("abc@1.com"))
        self.assertTrue(validate.validateEmail("abc@gmail.com.com"))

    def test_givenInvalidEmail_shouldReturnFalse(self):
        '''
        Description:
            The given invalid Email should return false in test case
        Parameter:
            It takes self as a parameter.
        '''

        self.assertFalse(validate.validateEmail("ranjith@.com"))
        self.assertFalse(validate.validateEmail("ran@gmail"))
        self.assertFalse(validate.validateEmail("ranji..28@gmail.com"))
        self.assertFalse(validate.validateEmail("ranjith123@gmail.c"))
        self.assertFalse(validate.validateEmail("aun@arc@gmail.com"))
        self.assertFalse(validate.validateEmail(".arun@@gmail.com"))

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
        
        self.assertTrue(validate.validatePassword("Arun@ranjith12"))
        self.assertTrue(validate.validatePassword("Rrunranjith1234@"))

    def test_givenInValidPassword_shouldReturnFalse(self):
        """
        Description:
            The given Invalid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertFalse(validate.validatePassword("arunranjith12"))
        self.assertFalse(validate.validatePassword("arunran"))
        self.assertFalse(validate.validatePassword("1ARUnRa"))
        self.assertFalse(validate.validatePassword("1234567"))
        self.assertFalse(validate.validatePassword("!@#$%1a"))

    

