class Rectangle:
    def __init__(self, width, height , ):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

   

t1= Rectangle(5, 10)
t2 = Rectangle(3, 4)
print("Area:", t1.area())
print("Area:", t2.area())