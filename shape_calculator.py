class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, width):
        self.height = width
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.width > 50) or (self.height) > 50:
            return "Too big for picture."
        else:
            picture = ""
            for _ in range(0, self.height):
                for _ in range(0, self.width):
                    picture += "*"
                picture += "\n"
            return picture

    def get_amount_inside(self, shape):
        area_1 = self.get_area()
        area_2 = shape.get_area()
        return int(area_1/area_2)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"{type(self).__name__}(side={self.width})"    

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)