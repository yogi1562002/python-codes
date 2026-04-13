# Print multiplication table of a given number
a= int(input("Enter a number for a table : "))
i = 1
while i<=10:
    print(f"{a} X {i} = {i*a}")
    i = i+1