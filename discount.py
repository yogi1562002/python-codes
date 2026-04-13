bill = int(input("Enter the bill amount : "))
if bill<1000:
    print(f"the bill amount is :{bill - (bill*(5/100))}")
elif bill>=1000 and bill<5000:
    print(f"the bill amout is : {bill-(bill*(10/100))}")
elif bill>=5000:
    print(f"the bill amount is : {bill-(bill*(20/100))}")
else:
    print("there is no discount ")