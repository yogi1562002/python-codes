#  Print numbers divisible by 5 up to n
num = int(input("Enter the final range : "))
i = 0
while num>i:
    i = i+1
    if i%5==0:
        print(i)
        
