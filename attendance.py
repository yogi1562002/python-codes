att = int(input("Enter your attendance percentage : "))
fee = input("Are paid fee  ( yes or no ):")
if fee == "yes" :
    if att >= 75:
        print("you are eligible for exam... ")
print("You are not eligible for exam...")