#wite a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle
from math import pi


class circle:
    def __init__(self):
        self.radius = float(input("Enter Radius of Circle : "))

    def compute_area(self):
        print("Area of circle is : ", pi * self.radius * self.radius)

    def compute_perimeter(self):
        print("Perimeter of circle is : ", 2 * pi * self.radius)

 
cr = circle()
cr.compute_area()
cr.compute_perimeter()