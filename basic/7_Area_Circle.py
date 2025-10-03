import math
def circle_area(r):
    return math.pi * r ** 2
radius = float(input("Enter radius: "))
print("Area of circle:", circle_area(radius))
