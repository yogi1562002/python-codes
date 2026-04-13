a = int(input("Enter the base value : "))
r = int(input("Enter r value : "))
n = int(input("Enter no of terms you want : "))
i = 0
while n>i:
    
    tn = a*r**(i)
    i=i+1
    print(tn)