class Cell:
   def __init__(self, elem):
     self.elem = elem

   def make_order (self, rows):
      return '\n'.join([' * ' * rows for _ in range(self.elem // rows)]) + '\n' + '*' * (self.elem % rows)

   def __str__(self):
      return str(self.elem)

   def __add__(self, other):
      return  'Sum of cell is ' + str(self.elem + other.elem)

   def __sub__ (self, other):
      return self.elem - other.elem if self.elem - other.elem >= 0 else 'cells in first cells less or equal second'

   def __mul__ (self, other):
     return 'Multiply of cells is' + str(self.elem * other.elem)

   def __truediv__ (self, other):
     return 'Truediv of cells is' + str(round(self.elem / other.elem))


cell_1 = Cell(5)
cell_2 = Cell(11)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))