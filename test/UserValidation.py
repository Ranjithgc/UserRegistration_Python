"""
@Author: Ranjith G C
@Date: 2021-07-07
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-07 
@Title : Program Aim is to validate user entered details using regular expression.
"""
import re

from loggers import logger

class Validation:

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
            if (re.match("^[A-Z]{1}[a-z]{2,}$",name)):
                return True
            else:
                return False
        
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
            
            if (re.match("^([a-z]{2,}[0-9a-z]{1,}([_+-.*$#]{0,1}[a-z0-9]{1,}){0,1}[@]{1}[a-z0-1]{1,}[.]{1}[a-z]{2,4}([.]{0,1}[a-z]{2,3}){0,1})$", email)):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)
