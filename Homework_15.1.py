class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total = self.get_square() + other.get_square()
            n_width = self.width + other.width
            n_height = total / n_width
            return Rectangle(n_width, n_height)
        raise ValueError

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            n_area = self.get_square() * n
            aspect_ratio = self.width / self.height
            n_width = (n_area * aspect_ratio) ** 0.5
            n_height = n_area / n_width
            return Rectangle(n_width, n_height)
        raise ValueError

    def __rmul__(self, n):
        return self.__mul__(n)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
