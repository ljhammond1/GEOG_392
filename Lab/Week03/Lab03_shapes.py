class Shape(): # DO I NEED TO GET RID OF COLOR?
    def __init__(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width)
        self.l = length
        self.w = Width

    def getArea(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, radius):
        self.r= radius

    def getArea(self):
        return 3.14 * self.r * self.r

class Triangle(Shape):
    def __init__(self, base, height):
        self.b = base
        self.h = height

    def getArea(self):
        return 0.5 * self.b * self.h


file = open(r'\Lab\Week03\shape_info.txt', 'r')
lines = file.readlines()
file.close()

totalShapes = []

for line in lines:
    components = line.split(",")
    Shape = components[0]

    if Shape == 'Rectangle':
        x = int(components[1])
        y = int(components[2])
        totalShapes
     elif Shape ==:
        pass

    if Shape == 'Triangle':
        print (Triangle.getArea())
    elif :
        pass
