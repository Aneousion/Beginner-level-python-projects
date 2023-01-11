print("""

Welcome to the Leap Year Calculator
From github.com/aneousion

""")

year = int(input("Which year would you like to check?"))  # input the year, int() converts the year to an integer
if year % 4 == 0:                                         # if the year is evenly divided by 4, if it's not it is not a leap year
    if year % 100 == 0:                                   # and is also evenly divided by 100, if it's not it is not a leap year
        if year % 400 == 0:                               # and is also evenly divided by 400, it is a leap year
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
