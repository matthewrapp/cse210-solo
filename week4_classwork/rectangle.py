class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height


rect2 = Rectangle(30, 20)
print('Rect2 Width: ', rect2.width, 'Rect2 Height: ', rect2.height)

rect2.setWidth(10)
print('Rect 2 New Width: ', rect2.getWidth())
print('Rect 2 Area: ', rect2.area())
