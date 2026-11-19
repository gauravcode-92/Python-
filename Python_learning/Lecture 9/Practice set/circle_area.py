class circle:
    def Area(self,radius):
        self.radius=radius
        pi=3.14
        area = pi * radius * radius
        print("Area of this radius is:",area)

    def Perimeter(self,radius):
        self.radius=radius
        pi=3.14
        perimeter=2 * pi * radius
        print("Perimeter of circle is:", perimeter)

cir1=circle()
cir1.Area(4)
cir1.Perimeter(5)

