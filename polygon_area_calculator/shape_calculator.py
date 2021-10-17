class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    shape = []
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        shape.append(self.width * "*" + "\n")
      return "".join(shape)

  def get_amount_inside(self, shape):
    fits = (self.width // shape.width) * (self.height // shape.height)
    return fits

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=" + str(self.width)+ ")"


  def set_side(self, side):
    self.width = side
    self.height = side