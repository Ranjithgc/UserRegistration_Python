class Sample:
   
    # input for invalid Name
    valid_name = [("Ranjith",True),("Rian",True)]

    # input for invalid Name
    invalid_name = [("Ra", False),
                      ("ranjith", False),
                      ("RANJITH", False),
                      ("Ra783", False),
                      ("R@anjith", False)]

    valid_email = [("ranjith1@yahoo.com", True), ("ranjith-100@yahoo.com", True), ("ran.100@yahoo.com", True), 
                   ("arun111@abc.com", True), ("arun-100@abc.net", True), ("arunra.100@abc.com.au", True), 
                   ("abc@1.com", True), ("abc@gmail.com.com", True)]
    
    inValid_email = [("ranjith@.com", False), ("ran@gmail", False), ("ranji..28@gmail.com", False), ("ranjith123@gmail.c", False), 
                     ("aun@arc@gmail.com", False), (".arun@@gmail.com", False)]

    valid_number = [("+91-8618663565", True), ("+91 9164222409", True)]

    inValid_number = [("+91-874543", False), ("+91-0432346578", False), ("+91 572781254324", False), 
                     ("7865438768",  False), ("+91  6587654324", False), ("+91-876365r324", False), 
                     ("+91-87656@r324", False)]

    valid_password = [("Arunr@njith1", True), ("Rrunranjith1234@", True)]

    inValid_password = [("Arunranjth", False), ("arunranjith12", False), ("1ARUnRa", False), ("1234567", False), ("!@#$1a", False)]