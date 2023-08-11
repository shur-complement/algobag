# Naive Dense Matrix Multiplication
# Time: O(N^3)

class DenseMatrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data

    def __getitem__(self, k):
        i, j = k
        return self.data[i][j]

    def __setitem__(self, k, v):
        i, j = k
        self.data[i][j] = v

    def __repr__(self):
        return repr(self.data)

def matmul_into(A,B,C):
    for i in range(A.rows):
        for j in range(B.cols):
            for k in range(A.cols):
                C[i,j] += A[i,k] * B[k,j]

A = DenseMatrix(
    3,4,
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
)

B = DenseMatrix(
    4,3,
    [[1,2,3],
     [4,5,6],
     [7,8,9],
     [10,11,12]]
)

C = DenseMatrix(3,3, [[0]*3 for _ in range(3)])
matmul_into(A,B,C)
print(C)
