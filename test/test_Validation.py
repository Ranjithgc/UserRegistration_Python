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
        