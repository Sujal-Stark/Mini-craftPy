print("Welcome to file Controller Programe.....\nInitaiting the Process")
print("\n1 = only read file.\n2 = only write file.\n10 = terminate")
print("Enter Command: ")
command = int(input())
while command != 10:
    if(command == 1):
        print("Enter File Name/Address: ")
        fileAddress = open(input(),"rt")
        content = " "
        print("The content of the file is:")
        while content != "":
            content = fileAddress.readline()
            print(content)
        fileAddress.close()
        print("Requested opeation is completed. \nEnter Command: ")
        command = int(input())
    elif(command == 2):
        print("Enter FIle name or Addrees: ")
        draftName = input()
        fileAddress = open(draftName,"a")
        print("Enter 0 for start writing mode.....\n Enter 2 to stop writing mode....")
        mode = int(input())
        while mode != 2:
            print("Enter Information: ")
            fileAddress.write("\n")
            fileAddress.write(input())
            fileAddress.close()
            print("Your Information is stored..... Enter Mode: ")
            print("3 --> read the update....\n 4 --> escape reading...\nEnter mode:")
            subMode = int(input())
            if(subMode == 3):
                cheakFileAddress = open(draftName)
                content = " "
                print("The content of the file is:")
                while content != "":
                    content = cheakFileAddress.readline()
                    print(content)
            elif(subMode == 4):
                cheakFileAddress.close()
            else:
                cheakFileAddress.close()
                print("Didn't find any command...\nAccess denied....")
            print("Want to write press 0, press 2 to stop")
            mode = int(input())
        print("Enter Command: ")
        command = int(input())
    else:
        print("Command not found......\nEnter valid command: ")
        command = int(input())
print("Programe is terminated....")