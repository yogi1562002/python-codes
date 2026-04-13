age = int(input("Enter your age : "))
ticketprice = int(input("Enter the ticket price : "))
if age < 5 :
    print(f"the price of the ticket is : free")
elif age>=5 and age<=12:
    print(f"The price of the ticket is : {ticketprice*(50/100)}/-")
elif age>=13 and age<=50:
    print(f"the price of the ticket is : {ticketprice}")
else:
    print(f"the price of the ticket is :{ticketprice*(60/100)}")


