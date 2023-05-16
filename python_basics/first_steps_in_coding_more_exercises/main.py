class Rhombus:
    def __init__(self, diagonal_length):
        self.diagonal_length = diagonal_length

    def draw_rhombus(self):
        if self.diagonal_length % 2 == 0:
            raise ValueError("Diagonal length must be odd")

        half_length = (self.diagonal_length + 1) // 2

        for i in range(1, half_length + 1):
            print(" " * (half_length - i) + "*" * (2 * i - 1))

        for i in range(half_length - 1, 0, -1):
            print(" " * (half_length - i) + "*" * (2 * i - 1))


stars = int(input('Input number of stars in diagonal: '))

r = Rhombus(stars)

r.draw_rhombus()
