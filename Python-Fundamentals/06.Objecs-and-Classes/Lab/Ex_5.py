class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle):
        return self.calculate_area() * angle / 360

    def results(self):
        return f"{self.calculate_circumference():.2f}\n"\
               f"{self.calculate_area():.2f}\n" \
               f"{self.calculate_area_of_sector(5):.2f}"


circle = Circle(10)

print(circle.results())
