# define parent class Shape, including the self argument so something else can be placed inside
class Shape(): 
    def __init__(self):
        pass

# define subclasses Rectangle, Circle, and Triangle
# use __init__ and include the self argument 
# include & define arguments for the measurements needed to calculate area (height, width, length, radius, etc.)
# define the getArea function for that specific shape subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    def getArea(self):
        return self.l * self.w
class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    def getArea(self):
        return 3.14 * self.r * self.r
class Triangle(Shape):
    def __init__(self, base, height):
        self.b = base
        self.h = height
    def getArea(self):
        return 0.5 * self.b * self.h

# open the shapes .txt file so the data entries can be read in
# read the lines of the file
# close the file
file = open(r'Hammond_GEOG392/Lab/Week03/shape_info.txt', 'r')
lines = file.readlines()
file.close()

# declare a set that the shapes from the file will fill
totalShapes = []

# for each line in the shapes .txt file, read components by splitting them at commas
# make shape designation (triangle, rectangle, or circle) is index 0, or the first argument, and its own object 
for line in lines:
    components = line.split(",")
    Shape = components[0]
#iterate through the list and determine the area for each individual shape based on above defined area functions
    if Shape == 'Rectangle':
        x = int(components[1])
        y = int(components[2])
        totalShapes.append(Rectangle(x,y)) #append actual shape instance here
    elif Shape == 'Circle':
        x = int(components[1])
        totalShapes.append(Circle(x))
    elif Shape == 'Triangle':
        x = int(components[1])
        y = int(components[2])
        totalShapes.append(Triangle(x,y))
    else:
        pass
# print each shape area
for shape in totalShapes:
    print(shape.getArea())

print('Printing Finished')
