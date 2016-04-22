def name_color():
    n = []
    c = []
    get_name_color(n, c)
    print_name_color(n, c)


def get_name_color(name, color):
    print("")
    print("* * * * * Hello. Welcome to the FavColor Game. * * * * *")
    print("")
    print("My name is Latasha and my favorite color is turquoise")
    print("")
    answer = "Y"
#    while ((answer != "Q") or (answer != "q")):
    while answer != "Q":

        name.append(input("What is your name? "))
        color.append(input("What is your favorite color? "))
        answer = input("If you'd like to quit the FavColor game, enter 'Q' or 'q'; to continue, enter any character ")
    print("")

def print_name_color(name, color):
    length = len(name)
    for i in range(0, length):
        print(name[i]+"'s favorite color is "+color[i])
    print("")
    print("* * * Thanks for playing the FavColor game * * *")

name_color()
