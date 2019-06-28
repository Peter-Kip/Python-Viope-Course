# -*- coding: cp1252 -*-

#asking for the number
number = input("Give a number: ")

#converting the number to integer
try:
    number = int(number)
    print("The input was suitable!")

#cathing the error - using Exception
except Exception:
    print("The input was malformed.")
    

