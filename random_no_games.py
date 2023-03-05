# computer number is guess and games
while 1:
    computerNumber = 4
    print("please guess my computer number.")

    yourNubmer = int(input("Enter your guess number : "))
    if yourNubmer == computerNumber:
        print("Congratulation!")
    else:
        print("You have lost")