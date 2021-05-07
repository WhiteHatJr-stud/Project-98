def swappingFiles():
    fileName1 = input("Enter the file name you want to swap: ")
    f1 = open(fileName1, "r")
    data_a = f1.read()

    fileName2 = input("Enter the other file name you want to swap: ")
    f2 = open(fileName2, "r")
    data_b = f2.read()

    f11 = open(fileName1, "w")
    f11.write(data_b)
    
    f22 = open(fileName2, "w")
    f22.write(data_a)

swappingFiles()