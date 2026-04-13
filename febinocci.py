# 0, 1, 1, 2, 3, 5, 8, 13, 21 …
# febinocci series upto n range 
num = int(input("Enter the series range : "))
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c