class Shapes:
    def __init__(self,name,side):
        self.name=name
        self.side=side
    def Area(self):
        print("I am a :" + self.name + "\n" +
              "I have" + self.side + "sides")


class Rectangle(Shapes):
    def __init__(self,len1,width1):
        self.len1=len1
        self.width1=width1
    def Area(self):
        result = self.len1*self.width1
        return result

class Circile(Shapes):
    def __init__(self,radius):
        self.radius= radius
    def Circle_Area(self):
        circle_area = 3.14*(self.radius)**2
        return circle_area
obj_area= Circile(5)
print("The area of a circle is:", obj_area.Circle_Area())

class Triangle(Shapes):
    def __init__(self,base,height):
        self.base=base
        self.height =height

    def Area_Triangle(self):
        area_triangle= 0.5*self.base*self.height
        return area_triangle

obj_triangle= Triangle(15,6)
print("The area of the triangle is ", obj_triangle.Area_Triangle())

