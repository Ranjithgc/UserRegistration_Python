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