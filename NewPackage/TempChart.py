'''
1.Write a program that outputs a table of Celsius temperatures from 0-100, in increments of 5.
2.In addition the corresponding Fahrenheit temperature should be listed
3.Upload code to your GitHub
'''

def DisplayTableofTemps():
#    global ctemp
#    ctemp=0
#    for ctemp in range (0,105,5):
#        print(ctemp," ",(ctemp*1.8)+32)
#        ctemp+=5


    ctemp=0
    while(ctemp <= 100):
        print(ctemp, "C  ", end="")
        if (len(str(ctemp)) == 1):
             print("   ", end="")
        elif (len(str(ctemp)) == 2):
            print("  ", end="")
        else:
            print(" ", end="")
        print((ctemp*1.8)+32, "F "  )
        print("")
        ctemp+=5

DisplayTableofTemps()