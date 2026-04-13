n = int(input("Enter no words: "))
li1 = []
for i in range(n):
    li1.append(input("Enter words : "))
li2 = []
for i in range(n):
    li2.append(input("Enter the number : "))
li3 = sorted(li2)
li4 = []
for i in range(len(li1)):
    li4.append(li1[i]+li3[i])
res = " ".join(li4)
print(res)

