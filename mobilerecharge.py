print("""mobile recharge plans :-
(1).basic plan---199  (1gb/day 28 days)
(2).standard plan --- 399 (1.5gb/day 56 days)
(3).premium plan ---599 (2gb/day 85 days)""")
budget = int(input("Enter your budget : "))
if budget >=200 and budget<=400:
    print("""recommended plan : basic plan
    validity : 28 days 
    data : 1gb/day
    calls : unlimited""")
elif budget>400 and budget<=600:
    print("""recommended plan : standard plan
    validity : 56 days 
    data : 1.5gb/day
    calls : unlimited""")
elif budget>600 :
    print("""recommended plan : premium plan
    validity : 85 days 
    data : 2gb/day
    calls : unlimited""")
else:
    print("you have no sufficient funds....")