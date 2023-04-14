class Circle:
    pi = 3.14159

    def __init__(self, diameter):
        self.diameter = diameter

    def Perimeter(self):
        return  Circle.pi * self.diameter

    def Area(self):
        return 0.25 * Circle.pi * self.diameter ** 2

    def Display(self):
        print(f"The perimeter of the circle is: {self.Perimeter():}")
        print(f"The area of the circle is: {self.Area():}")


diameter = float(input("Enter the diameter of the circle: "))

circle = Circle(diameter)

circle.Display()