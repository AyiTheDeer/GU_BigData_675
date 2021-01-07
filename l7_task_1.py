class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in self.matrix:
            print(i)

    def __add__(self, other):
        result = []
        for i in zip(self.matrix, other.matrix):
            a = [x + y for x, y in zip(i[0], i[1])]
            result.append(a)
        return Matrix(result)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 1, 1], [0, 0, 0], [2, 2, 2]])
c = a + b
print(c)