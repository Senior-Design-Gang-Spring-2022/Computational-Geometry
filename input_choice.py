
from ftplib import all_errors
from multiprocessing.sharedctypes import Value
import string
from points import Point
from lines import Line_Segment

def InputChoice(choice = None): 
    if (choice is not None): 
        try: 
            picked = int(choice)
        except ValueError: 
            return 0
        if (picked is not None and picked < 1 or picked > 3): 
            return 0
        elif (picked >= 1 and picked <= 3): 
            return picked
    
    elif (choice == None): 
        print("Pick values from 1 to 3: ") 
        print("1 : Input points one by one")
        print("2 : Use a CSV file") 
        print("3 : Use template values")
        try: 
            picked = int((input("Pick values from 1 to 3")))
        except all_errors: 
            return 0

        if (picked > 3 or picked <1): 
            return 0
        else: 
            return picked
             
    else: 
        print("Entered an invalid argument.")
        return 0
