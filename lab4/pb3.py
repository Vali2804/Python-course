
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for j in range(m)] for i in range(n)]

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transposed = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                transposed[j][i] = self.matrix[i][j]
        self.matrix = transposed
        self.n, self.m = self.m, self.n

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Matrices cannot be multiplied")
        result = [[0 for j in range(other.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def transform(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = func(self.matrix[i][j])
    


#a testing function
def main():
    m = Matrix(3, 3)
    m.set(0, 0, 1)
    m.set(0, 1, 2)
    m.set(0, 2, 3)
    m.set(1, 0, 4)
    m.set(1, 1, 5)
    m.set(1, 2, 6)
    m.set(2, 0, 7)
    m.set(2, 1, 8)
    m.set(2, 2, 9)
    print("matrix m")
    print(m.matrix)
    m.transform(lambda x: x + 1)
    print("matrix m + 1")
    print(m.matrix)
    m.transpose()
    print("matrix m transposed")
    print(m.matrix)
    m2 = Matrix(3, 2)
    m2.set(0, 0, 1)
    m2.set(0, 1, 2)
    m2.set(1, 0, 3)
    m2.set(1, 1, 4)
    m2.set(2, 0, 5)
    m2.set(2, 1, 6)
    print("matrix m2")
    print(m2.matrix)
    print("matrix m * m2")
    print(m.multiply(m2))

if __name__ == "__main__":
    main()
    