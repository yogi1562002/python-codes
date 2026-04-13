std = input("Are you a student (yes / no ) : ")
if std.lower() == "yes":
    age = int(input("Enter your age : "))
    if age<=18:
        print("you are  eligible for the buss pass" )
    else:
        print ("you are not eligible for buspass")
else:
    print ("you are not eligible for buspass")