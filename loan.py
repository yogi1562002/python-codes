#Bank loan eligibility based on salary & credit score
sal = int(input("Enter your salary per month : "))
credit_score = int(input("Enter your credit score ( 0 - 1000 ) : "))
if sal > 50000 and credit_score > 600:
    print("you are eligible for the loan...")
else:
    print("you are not eligible for the loan...")