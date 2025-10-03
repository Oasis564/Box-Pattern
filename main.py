import math
# write the code to calculate the circumference of a circle

# formula 1= C=Pie*Diameter
#  formula 2= C=2*Pie*radius

def c1(diameter):
    result = 3.14159265359*diameter
    print("The circumference of the circle using formula 1 was, ", round(result, 2))
    
def c2(radius):
    result = 2*math.pi*radius
    print("The circumference of the circle using formula 2 was, ", round(result, 2))
    
diameter = float(input("What is the diamater of the circle?"))
radius = float(input("What is the radius of the circle?"))


c1(diameter)
c2(radius)
