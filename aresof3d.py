print("""(1).cuboid
(2).cube
(3).cylinder
(4).cone
(5).sphere
(6).Hemisphere""")
choice = int (input("Enter you choice : "))
if choice == 1:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice1 = int(input("enter your choice :"))
    length = float(input("Enter the length of the cuboid : "))
    breadth = float(input("Enter the breadth of the cuboid : "))
    height = float(input("Enter the height of the cuboid : "))
    if choice1==1:
        print(f"The curved surface area of cuboid is : {2*height(length+breadth)}")
    elif choice1==2:
        print(f"the total surface area of a cuboid is : {2*((length*breadth)+(breadth*height)+(height+length))}")
    else:
        print(f"the volume of the cuboid is : {length*breadth*height}")
    breakpoint
if choice==2:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice2 = int(input("enter your choice :"))
    s = float(input("Enter the side of a cube : "))
    if choice2==1:
        print(f"The curved surface area of cube is : {4*(s)**2}")
    elif choice2==2:
        print(f"the total surface area of a cube is : {6*(s)**2}")
    else:
        print(f"the volume of the cube is : {s**3}")
    breakpoint
if choice == 3:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice3 = int(input("enter your choice :"))
    r = float(input("Enter the radius of the cylinder : "))
    h = float(input("Enter the height of the cylinder : "))
    if choice3==1:
        print(f"The curved surface area of cylinder is : {2*3.14*r*h}")
    elif choice3==2:
        print(f"the total surface area of a cylinder is : {2*3.14*r*(r+h)}")
    else:
        print(f"the volume of the cylinder is : {3.14*((r)**2)*h}")
    breakpoint
if choice == 4:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice4 = int(input("enter your choice :"))
    l = float(input("Enter the length of the cone : "))
    r = float(input("Enter the radius of the cone : "))
    if choice4==1:
        print(f"The curved surface area of cone is : {3.14*r*l}")
    elif choice4==2:
        print(f"the total surface area of a cone is : {3.14*r*(l+r)}")
    else:
        print(f"the volume of the cone is : {1/3*3.14*((r)**2)*h}")
    breakpoint
if choice ==5:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice5 = int(input("enter your choice :"))
    r = float(input("Enter the radius of the sphere : "))
    if choice5==1:
        print("there is no curved area for a sphere")
    elif choice5==2:
        print(f"the total surface area of a sphere is : {4*3.14*((r)**2)}")
    else:
        print(f"the volume of the sphere is : {(4/3)*3.14*((r)**3)}")
    breakpoint
if choice == 6:
    print("""(1).curved surface area
    (2).Total surface area
    (3).volume""")
    choice6 = int(input("enter your choice :"))
    r = float(input("Enter the radius of the hemisphere : "))
    
    if choice6==1:
        print(f"The curved surface area of hemisphere is : {2*3.14*((r)**2)}")
    elif choice6==2:
        print(f"the total surface area of a hemisphere is : {3*3.14*((r)**2)}")
    else:
        print(f"the volume of the hemesphere is : {(2/3)*3.14*((r)**3)}")
    breakpoint