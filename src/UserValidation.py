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
    def __init__(self) -> None:
        pass

    def validateName(self, name):
        '''
        Description:
            This method is used for validating name with regex pattern.
        Parameter:
            it takes name and self as parameter
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

    def input(self):
        '''
        Description:
            This method is used for getting user input frm the user.
            It calls the validate name method of validate user class 
            for validation of firstname, lastname, email.
        '''

        try:
            
            firstName = input("Enter your First Name: ")
            logger.info(self.validateName(firstName))

            lastName = input("Enter Users Last Name")
            logger.info(self.validateName(lastName))
            
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    validate = Validation()
    validate.input()        

