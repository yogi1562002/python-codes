a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
operation =input("enter the operation (+,-,*,/,%,//) : ")
if operation == "+" : 
    print(a+b)
elif operation == "-" :
    print(a-b)
elif operation == "*" :
    print(a*b)
elif operation == "/" :
    print(a/b)
elif operation == "%" :
    print(a%b)
elif operation == "//" :
    print(a//b)
else:
    print("Enter a valid operation")
