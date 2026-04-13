num = int(input("Enter a number : "))
if num%5==0:
    if num%11==0:
        print("the given number is divisible by the 5 and 11...")
    else:
        print("the given number is divisible by 5 and not divisible by 11...")
else:
    print("the number is not divisible by the 5 and 11...")