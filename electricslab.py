units = int(input("Enter consumed units used :"))
if units<=100:
    print(f"the bill amount is : {units*2}")
elif units<=300:
    print(f"the bill amount is : {200+((units-100)*3)}")
elif units<=500:
    print(f"the bill amount is : {200+300+((units-200)*5)}")
elif units>500:
    print(f"the bill amount is : {1000+((units-300)*7)}")