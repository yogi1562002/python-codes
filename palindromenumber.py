num = int(input("enter your number:"))
temp = num
rev = 0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
if rev==temp:
    print("palidrome")
else:
    print("not a palindrome")



n = input("Enter your number:")
res = n[::-1]
if res == n:
    print("palindrome")
else:
    print("not a palindrome")
    