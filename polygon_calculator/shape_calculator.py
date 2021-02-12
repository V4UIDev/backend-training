class Rectangle:
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
    
    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width + self.width + self.height + self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def __str__(self):
        return("Rectangle(width=" + str(self.width) + ", " + "height=" + str(self.height) + ")")

    def get_picture(self):

        n = 0
        widthString = ""
        image = ""

        if self.width > 50 or self.height > 50:
            image = "Too big for picture."
            return image

        while n < self.width:
            widthString = widthString + "*"
            n = n + 1
        n = 0

        while n < self.height:
            image = image + widthString + "\n"
            n = n + 1
        while n == self.height - 2:
            image = image + widthString
            n = n + 1

        return image

    def get_amount_inside(self, shape):
        if shape.height > self.height and shape.height > self.width:
            return 0
        elif shape.width > self.width and shape.width > self.height:
            return 0
        calcHeight = int(self.height) / int(shape.height)
        calcWidth = int(self.width) / int(shape.width)

        ansWidth = calcHeight * calcWidth
        return int(ansWidth)






class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return("Square(side=" + str(self.width) + ")")

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.height = width

    
