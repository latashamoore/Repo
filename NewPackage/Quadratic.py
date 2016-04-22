"""
Assignment # 3.2- Quadratic
Overview
You are interested in creating a program that will solve for the value of a quadratic.
A quadratic follows the format of AX2 +BX + C (A,B,C are variables)
Write a small python program that does the following:
*Ask the user to enter the value of A,B,C and X.
*Your program will then calculate the value of the quadratic.
*Your program should output the quadratic along with the value of the quadratic.(See sample output). Check your math!

%%%%
You should test your programs for multiple combinations of positive and negative values of all variables.
Attach screenshots of at least 4 different combinations.
Upload your code to Git Hub.

3X^2+2-8X+4
AX^2 + BX + C
%%%% For all unknown variables, Never take floats, only take integer inputs %%%%
%%%% aValue must never be zero; otherwise, it would be a linear equation, not a quadratic one %%%%

"""


def display_intro():
    print("    * * * * * Welcome to the Quadratic program! * * * * *    ")
    print(" Please enter the values of A, B, C, X at the corresponding prompts. ")
    print("")


def get_values(a_value, b_value, c_value, x_value):
    print(a_value,b_value,c_value,x_value)
    got_values = False
    while got_values == False:
        try:
            a_value = int(input("Please enter a non-negative integer value for A. "))
            while a_value == 0:
                a_value = int(input("Correct your last entry and make sure to enter a non-negative integer value for A. "))
            b_value = int(input("Please enter an integer value for B? "))
            c_value = int(input("Please enter an integer value for C? "))
            x_value = int(input("Please enter an integer value for X? "))
            got_values == True
        except:
            print("Please make sure to only enter valid integer values")

def calculate_quadratic_value(a_value, b_value, c_value, x_value):
    return ((a_value * (x_value * x_value)) + (b_value * x_value) + c_value)


def display_equation_and_value(a_value, b_value, c_value, x_value):
    print("")
    #AX^2 + BX + C
    #Make sure to subtract if B is negative, ie, AX^2 - BX + C
    if(b_value >= 0):
        print("The following quadratic equation was entered :  ", a_value, "X^2 + ", b_value, "X + ", c_value)
    else:
        print("The following quadratic equation was entered :  ", a_value, "X^2 - ", abs(b_value), "X + ", c_value)
    print("The value of the quadratic equation is ", float((a_value * (x_value * x_value)) + (b_value * x_value) + c_value))


def quadratic_equation():
    display_intro()
    global a
    a = 0
    global b
    b = 0
    global c
    c = 0
    global x
    x = 0
    get_values(a, b, c, x)
#   qvalue is not needed since its calculated later
#   qvalue = calculate_quadratic_value(a, b, c, x)
    display_equation_and_value(a, b, c, x)
