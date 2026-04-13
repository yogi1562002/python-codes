# Print arithmetic progression series
'''a = int(input("Enter a value : "))
d = int(input("Enter d value : "))
n = int(input("Enter the no of terms you want : "))
for i in range (0, n):
    an = a + (i*d)
    print(an)'''

a = int(input("Enter a value : "))
d = int(input("Enter d value : "))
n = int(input("Enter the no of terms you want : "))
i = 0
while n>i:
    an = a + (i*d)
    print (an) 
    i=i+1