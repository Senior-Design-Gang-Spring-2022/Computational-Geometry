from points import Point
from lines import Line_Segment

def InputChoice(choice): 
    picked = choice
    if (picked != None and picked <= 3 and picked >= 1): 
        return picked
    elif (choice == None): 
        print("Pick values from 1 to 3: ") 
        print("1 : Input points one by one")
        print("2 : Use a CSV file") 
        print("3 : Use template values") 
        input("Pick values from 1 to 3")
    else: 
        print("You did not enter a value from 1-3")
