"""
@Author: Ranjith G C
@Date: 2021-07-08
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-08 
@Title : Program Aim is to validate user entered details using regular expression.
"""

class EmailSamples:

    validEmails = ["ranjith10@yahoo.com", "ranjith-100@yahoo.com", "ran.100@yahoo.com", 
                   "arun111@abc.com", "arun-100@abc.net", "arunra.100@abc.com.au", 
                   "abc@1.com", "abc@gmail.com.com"]
    
    inValidEmails = ["ranjith@.com", "ran@gmail","ranji..28@gmail.com", "ranjith123@gmail.c", 
                     "aun@arc@gmail.com", ".arun@@gmail.com"]