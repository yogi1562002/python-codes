s= int(input("Enter no of numbers: "))
s1 = set()
s2 = set()
s4 = set(sorted(s1))
print(s4)
s5 = set(sorted(s2))
for i in range(s):
    s1.add(int(input("Enter number : ")))
ss = int(input('Enter noof numbers : '))
for i in range(ss):
    s2.add(int(input("Enter numbers : "))) 
a = s4.union(s5)
print(a)