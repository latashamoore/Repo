def main():
    answer = "Y"
    while (answer == "Y"):
        ftemp = int(GetTemp())
        ctemp = ConvertTemp(ftemp)
        print("Fahrenheit Temperature is", ftemp, "& Celsius Temperature is",str(ctemp)+".")
        answer = input("Would you like to convert another temperature? Enter 'Y' or 'N'")

def GetTemp():
    # return (input("Please enter a temperature you'd like to convert into celsius "))
    temperature = (input("Please enter a temperature you'd like to convert into celsius "))
    return temperature

def ConvertTemp(fahrenheit):
    return ((fahrenheit - 32) / 1.8)


main()
