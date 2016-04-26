def main():
    try:
        f = open("C:/Users/Student 2/Documents/Assignment1.txt", "r")
        print(f.read(1))
        print(f.readline())
        print(f.read())
        f.close()
    except:
        print("Error opening file")

    f2 = open("C:/Users/Student 2/Documents.txt", "r")
    my_list = []
    for line in f2:
        my_list.append(line)
    print(my_list)
    f2.close()

    f3 = open("C:/Users/Student 2/Documents.txt", "r")
    my_list3 = []
    for line in f3:
        my_list3.append(line)
        for a in range(0,b):
            print(my_list3[a])
    f3.close()

main()
