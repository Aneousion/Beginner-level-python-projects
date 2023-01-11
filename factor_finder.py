print("""

Welcome to the factor finder
From github.com/aneousion

""")

# input the number to be checked, int() converts the input to an integer. "\n" enters a new line
number = int(input("Enter the number to be checked: \n"))

# create an empty variable to store the factors
factors = ""

for i in range(1, number + 1):        # test number = 8, loops through 1 and 9
    if number % i == 0:               # if any number between 1 and 9 can evenly divide 8, that is, it is a factor of 8
        if i == number:               # if 8 == 8
            factors += str(i) + "."   # saves the number into the factor variable
            break                     # exits the for loop
        factors += str(i) + ","       # saves the number into the factor variable

print(f"factors of {number} are {factors}")
