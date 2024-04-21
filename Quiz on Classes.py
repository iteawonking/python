#Quiz on Classes 김우준 2024133519

# Import the library
import matplotlib.pyplot as plt
%matplotlib inline 

# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    
    # Constructor 
    def __init__(self, width = 2, height = 3, color ='r'): 
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()



# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

# Print the object attribute height
SkinnyBlueRectangle.height

10

# Print the object attribute width
SkinnyBlueRectangle.width

2

# Print the object attribute color
SkinnyBlueRectangle.color

blue
# Use the drawRectangle method to draw the shape

SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle

FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Print the object attribute height
FatYellowRectangle.height

5

# Print the object attribute width
FatYellowRectangle.width

20

# Print the object attribute color
FatYellowRectangle.color

yellow

# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()
