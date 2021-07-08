"""
@Author: Ranjith G C
@Date: 2021-07-08
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-08 
@Title : Program Aim is to validate user entered details using regular expression.
"""
import re

from loggers import logger

class UserValidation:

    def validateName(name):
        '''
        Description:
            This method is used for validating name with regex pattern.
        Parameter:
            it takes name as parameter
        Return:
            It return a valid true if name is valid and false if it's invalid.
        '''

        try:
            return bool(re.match("^[A-Z]{1}[a-z]{2,}$",name))
        
        except Exception as e:
            logger.error(e)

    def validateEmail(email):
        '''
        Description:
            This function is used for validating email with regex pattern.
        Parameter:
            it takes self, email as parameters
        Return:
            It return a valid true if email is valid and false if it's invalid.
        '''

        try:
            
            return bool(re.match("^([a-z]{2,}[0-9a-z]{1,}([_+-.*$#]{0,1}[a-z0-9]{1,}){0,1}[@]{1}[a-z0-1]{1,}[.]{1}[a-z]{2,4}([.]{0,1}[a-z]{2,3}){0,1})$", email))

        except Exception as e:
            logger.error(e)

    def validateNumber(phone):
        '''
        Description:
            This function is used for validating mobile number with regex pattern.
        Parameter:
            it takes self, phone as parameters
        Return:
            It return a valid true if phone is valid and false if it's invalid.
        '''

        try:

            return bool(re.match("^[\+][9?][1?][\-\s]?[6-9]{1}[\d]{9}$", phone))
                
        except Exception as e:
            logger.error(e)

    def validatePassword(password):
        '''
        Description:
            This function is used for validating password with regex pattern.
        Parameter:
            it takes self, password as parameters
        Return:
            It return a valid true if password is valid and false if it's invalid.
        '''

        try:

            return bool(re.match("^(?=.*[@#$%^&+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$", password))
        
        except Exception as e:
            logger.error(e)