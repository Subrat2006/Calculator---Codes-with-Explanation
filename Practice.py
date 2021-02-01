# Today, We will do a Practice of Python Codes
# Let's Make a Calculator here

def Calculator(): #Here, we are defining a Function
# A function is a group of codes! When we call the function name, all the codes inside the Function are executed.
    a = float (input ("Enter the 1st number:- "))
    b = float (input ("Enter the 2nd number:- "))
    # Above codes describe the input as variables

    print ("Press 1 for Addition")
    print ("Press 2 for Subtraction")
    print ("Press 3 for Multiplication")
    print ("Press 4 for Division")
    # We are printing the above statements and will take their input as a variable named 'x'

    x = str (input ("Enter-> "))
    # Note: str means string values, float means Float values (numbers with decimals) and int means interger values (numbers without decimals)

    if x == '1': #Below are the code line for the addition
        print ("The sum of", a, 'and', b, 'is', a + b)
    elif x == '2': #Below are the code line for the Subtraction
        if a > b:
            print ("The difference between", a, 'and', b, 'is', a - b)
        elif a < b:
            print ("The difference between", b, 'and', a, 'is', b - a)
        else:
            print ("The difference between", a, 'and', b, 'is', a - b)
    elif x == '3': #Below are the code line for the Multiplication
        print ("The product of", a, 'and', b, 'is', a * b)
    elif x == '4': #Below are the code line for the Division
        if a > b:
            print ("The quotient while dividing", a, 'from', b, 'is', a / b)
        elif a < b:
            print ("The quotient while dividing", b, 'from', a, 'is', b / a)
        else:
            print ("The quotient while dividing", a, 'from', b, 'is', a / b)
    else: #Below are the code line for the numbers pressed by the user, other than 1, 2, 3, and 4.
        print ("Invalid Input")
        Calculator()
# Now the Function codes end

print ("Welcome to the Calculator") #This is the Welcome message
Calculator() #By this code, all the codes in the function are executed here.

while True: #This establishes an Infinite Loop
# An infinite loop is a loop which contiues till it's not breaked
    print ("Do you want to reuse the application?")
    print ("Press 1 for yes and 2 for No")

    s = str (input ("-> ")) #This is a variable assigned for the input by user [Yes or No]

    if s == '1': #Below are the codes which would be needed for restarting the calculator!
        print () #This leaves a space between
        Calculator() #This executes all the codes of Calculator
    elif s == '2':
        print ("Thank you for using the application!")
        break #This is the codes for BREAKING the INFINITE LOOP
    else:
        print ("Invalid Input")
        print ()
# Congratulations! Our Calculator is ready!
# This is a Calculator which will ask repeteadly for reusing the application (i.e., Calculator) till it's not cancelled.
