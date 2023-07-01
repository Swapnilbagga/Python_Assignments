import math
print("1: triangle")
print("2: rectangle")
print("3: circle")
choice=int(input("Enter the choice:"))
if choice==1:
    print("it is a triangle.")
    h=int(input("Enter the height:"))
    b=int(input("Enter the base:"))
    print("area:",area=(b*h)/2)
elif choice==2:
    print("it is a quadrilateral")
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    print("area",area=l*b)
elif choice==3:
    print("it is a circle")
    r=int(input("enter the radius"))
    print("area",area=math.pi*r**2)
else:
    print("enter the choice less than 4")