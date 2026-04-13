a = int(input("Enter no of numbers: "))
s1 = set()
s2 = set()
for i in range(a):
    s1.add(int(input("Enter a number in s1:")))
b = int(input("Enter no of numbrs : "))
for i in range(b):
    s2.add(int(input("Enter a number s2 :")))
if s1.isdisjoint(s2):
    print("Disjoint")
else:
    print("Not Disjoint")