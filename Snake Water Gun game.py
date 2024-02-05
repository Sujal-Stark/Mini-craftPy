import random
defaultLibrary = ["snake","water","gun"]
heart = 5 ; win = 0; terms = 0
while heart !=0:
    if win == 3:
        print("Congratulation! You Won the match....")
        break
    print("\n\nsnake ---> 0\nwater ---> 1\ngun ---> 2")
    choice = int(input("Enter choice: "))
    systemChoice = random.choice(defaultLibrary)
    if(defaultLibrary[choice]==systemChoice): print("draw!!!!\nTry Again....")
    else:
        if choice == 0: #snake by user
            if systemChoice == defaultLibrary[1]: #snake >water
                win += 1
                print(f"\nnumber of wins: {win}")
            elif systemChoice == defaultLibrary[2]: # gun>snake
                heart -=1
                print(f"\nNumber of hearts left: {heart}")
        elif choice == 1: #water by user
            if systemChoice == defaultLibrary[2]: # water>gun
                win += 1
                print(f"\nnumber of wins: {win}")
            elif systemChoice == defaultLibrary[0]: #snake>water
                heart -= 1
                print(f"\nNumber of hearts left: {heart}")
        elif choice == 2: #gun by user
            if systemChoice == defaultLibrary[0]: # gun>snake
                win += 1
                print(f"\nnumber of wins: {win}")
            elif systemChoice == defaultLibrary[1]: #water>gun
                heart -= 1
                print(f"\nNumber of hearts left: {heart}")
        else: #snake by user
            print("Wrong Input.......")
    terms += 1
    if heart == 0: print("You loose")
print(f"programme terminated with {terms} terms")