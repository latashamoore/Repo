"""
Assignment # 3.3- User Input
Overview
Given a set of numbers, create a program that returns the largest and smallest number in the set.
Do not use any existing python functions!
Write a small python program that does the following:
Accepts X amount of numbers from a user
Store each value in a list
Create one or more functions which return the maximum number in the list.
Create one or  more functions which return the smallest number in the list.
Upload your code to GitHub

Example
my_list = [5, 7, 15, 1, 8] ... min is 1; max is 15; sorted [1, 5, 7, 8, 15]
%%%% Set Min and Max to value of first index
max_num = my_list[0]
min_num = my_list[0]
compare other values to this first value

watch the index out of bounds exception
Bonus: Sort the list (DO NOT use the sort function)

"""


def find_min(array):
    minimum = array[0]
    length = len(array)
    for x in range(0,length):
        if minimum > array[x]:
            minimum = array[x]
    return minimum


def find_max(array):
    maximum = array[0]
    length = len(array)
    for x in range(0,length):
        if maximum < array[x]:
            maximum = array[x]
    return maximum


def find_min_max():
    print("")
    print("*** Largest/Smallest Numbers in the List ***")
    print("")
    my_list = []
    valid_input = False
    while valid_input == False:
        try:
            array_length = int(input("How many numbers would you like to add to the list? "))
            if array_length <= 0:
                print("Please enter a valid integer value above 0. ")
            valid_input = True
        except:
            print("Only valid integer values are accepted.")
    valid_input = False
    while valid_input == False:
        try:
            for x in range(0, array_length):
                my_list.append(int(input("Which number would you like to add to the list? ")))
                valid_input = True
        except:
            print("Please enter a valid integer value")

    smallest = find_min(my_list)
    print(smallest)
    largest = find_max(my_list)
    print(largest)
#    sort_list(my_list)
#    for i in range(0, array_length):


find_min_max()
