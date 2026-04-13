num= 12323242345435
count = 0
while num>0:
    digit = num%10
    count = count+1
    num = num//10
print(count)