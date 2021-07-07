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

    def validateEmail(self, email):
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

    def validateNumber(self, phone):
        '''
        Description:
            This function is used for validating mobile number with regex pattern.
        Parameter:
            it takes self, phone as parameters
        Return:
            It return a valid true if phone is valid and false if it's invalid.
        '''

        try:

            if(re.match("^[\+][9?][1?][\-\s]?[6-9]{1}[\d]{9}$", phone)):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)

    def validatePassword(self, password):
        '''
        Description:
            This function is used for validating password with regex pattern.
        Parameter:
            it takes self, password as parameters
        Return:
            It return a valid true if password is valid and false if it's invalid.
        '''

        try:

            if(re.match("^[a-z]{8,}$", password)):
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
            
            email = input("Enter Users Email ID")
            logger.info(self.validateEmail(email))

            phoneNumber = input("Enter Users Phone Number")
            logger.info(self.validateNumber(phoneNumber))

            password = input("Enter the Users Password")
            logger.info(self.validatePassword(password))
            
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    validate = Validation()
    validate.input()        

