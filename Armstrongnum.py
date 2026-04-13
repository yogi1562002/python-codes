num = int(input("Enter a number: "))
sum = 0
temp = num
n = len(str(num))
while num>0:
    digit = num%10
    sum = sum + digit**n
    num = num//10
if sum == temp:
    print("yes")
else:
    print("no")