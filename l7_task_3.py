class Cell:
    def __init__(self, cell_count):
        self.cell_count = int(cell_count)

    def __add__(self, other):
        return Cell(self.cell_count + other)

    def __sub__(self, other):
        return Cell(self.cell_count - other)

    def __mul__(self, other):
        return Cell(self.cell_count * other)

    def __truediv__(self, other):
        return Cell(int(self.cell_count / other))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell_count / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.cell_count % cells_in_row)}'
        return row


cell1 = Cell(10)
cell2 = Cell(5)
print(cell1.cell_count)
print(cell1.cell_count + cell2.cell_count)
print(cell1.cell_count / cell2.cell_count)
print(cell1.cell_count * cell2.cell_count)
print(cell1.make_order(3))