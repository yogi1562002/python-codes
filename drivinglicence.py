age = int(input("Enter your age : "))
if age <16:
    print("You are not eligible for driving licence...")
elif (16<=age) and (age<18):
    print ("You are eligible for gearless vechicle driving licence...")
elif (18<= age) and (age <=60):
    print ("You are eligible for gear vechicle driving licence...")
else:
    print("You are not eligibl