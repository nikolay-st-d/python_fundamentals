class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * self.__pi
        return circumference

    def calculate_area(self):
        radius = self.diameter / 2
        area = self.__pi * radius * radius
        return area

    def calculate_area_of_sector(self, angle):
        sector_area  = angle/360 * self.__pi * (self.diameter / 2) * (self.diameter / 2)
        return sector_area
