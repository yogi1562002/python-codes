# the code will says the given character is alphabet or number or special character 
char = input("Enter the character here: ")
if char.isalpha():
    print("the enter character is alphabet...")
elif char.isdigit():
    print("the entered character is digit...")
else:
    print ("Entered character is sepcial character...")
