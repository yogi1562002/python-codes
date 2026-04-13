print("""(1).kite
(2).trapezium
(3).parallelogram
(4). rectangle
(5).rhambous
(6). square
(7). circle""")
choice = int(input("Enter your choice : "))
if choice == 1:
    print("""(1).area of the kite
          (2).perimeter """)
    choice1 = int(input("Enter your choice: ")) 
    if choice1 ==1:
        d1=float(input("Enter the first diagonal length : "))
        d2=float(input("Enter the second diagonal length : "))
        print(f"Area of the kite is : {0.5*d1*d2}")
    else:
        s1=float(input("Enter the first side of the kite: "))
        s2=float(input("Enter the second side of the kite: "))
        print(f"perimeter of the kite is : {s1+s1+s2+s2}")
if choice ==2:
    print("""(1).area of the trapezium
          (2).perimeter of the trapezium""")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        b1=float(input("enter the valur of first base : "))
        b2=float(input("Enter the value of second base : "))
        h=float(input("Enter the height of the trapizium : "))
        print(f"the area of the trapezium is : {0.5*(b1+b2)*h}")
    else:
        s1=float(input("Enter the first side length : "))
        s2=float(input("Enter the second side length : "))
        s3=float(input("Enter the third side length : "))
        s4=float(input("Enter the fourth side length : "))
        print(f"the perimeter of the trapezium is : {s1+s2+s3+s4}")
if choice == 3:
    print("""(1).area of the parallelogram
          (2).perimeter of the parallelogram""")
    choice3 = int(input("enter your choice : "))
    if choice == 1:
        b=float(input("enter the breadth of the parallelogram : "))
        h = float(input("Enter the height of the parallelogram : "))
        print(f"the area of the parallelogram : {b*h}")
    else:
        s1 = float(input("Enter the first side of the parallelogram : "))
        s2 = float(input("Enter the second side of the parallelogram : "))
        print(f"The perimeter of the parallelogram is : {2*(s1+s2)}")
if choice == 4:
    print("""(1).area of the rectangle
          (2).perimeter of the rectangle """)
    choice4 = int(input("Enter your choice : "))
    if choice4 == 1:
        l = float(input("Enter the legth of the rectangle : "))
        b = float(input("Enter the breadth of the rectangle :  "))
        print(f"The area of the rectangle is : {l*b}")
    else:
         l = float(input("Enter the legth of the rectangle : "))
         b = float(input("Enter the breadth of the rectangle :  "))
         print(f"The perimeter of the rectangle is : {2*(l+b)}")
    
if choice ==5 :
     print("""(1).area of the rhombous
          (2).perimeter of the rhombous """)
     choice5=int(input("Enter your choice: "))
     if choice5==1:
         d1 = float(input("Enter the length of first diagonal of the rhombous: "))
         d2 = float(input("Enter the length of second diagonal of the rhombous: "))
         print(f"The area of a rhombus is: {0.5*d1*d2}")
     else:
         s = float(input("Enter the side of a rhmbous: "))
         print(f"The perimeter of the rhombus is :{4*s}")
if choice == 6:
    print("""(1).area of the square
          (2).perimeter of the square """)
    choice6 = int(input("Enter your choice: "))
    if choice6==1:
        s = float(input("Enter the side of a square : "))
        print(f"the area of the square is :{s*s}")
    else:
        s = float(input("Enter the side of a square : "))
        print(f"the perimeter of the square is : {4*s}")
if choice == 7:
    print("""(1).area of the circle
          (2).perimeter of the circle """)
    choice7 = int(input("enter your choice: "))
    if choice7 ==1 :
        r = float(input("enter the radius of the circle:  "))
        print(f"the area of the circle is : {3.14*r*r}")   
    else:
        print("now take the thread and put it starting point to ending point ") 