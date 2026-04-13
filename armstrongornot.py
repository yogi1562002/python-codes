number=int(input("enter a number : "))
temp=number
digits=len(str(number))
sum=0
while temp>0:
    digits=temp%10
    sum=sum+digits**digits
    temp//=10
if sum == number:
    print("yes")
