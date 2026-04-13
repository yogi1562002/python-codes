n = 10
for i in range(1,n):
    print(i, end = " ")
    if i%2!=0:
        print()
        continue
    print(i)
else:
    print("completed")