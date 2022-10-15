import numpy as np
def polynomial_multiplication(P, Q):
    m = len(P)
    n = len(Q)
    result = [0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            result[i+j] += P[i]*Q[j]
    return result
def polynomial(poly):
    n = len(poly)
    for i in range(n): 
        print(poly[i], end = "")
        if (i != 0): 
            print("x^", i, end = "") 
        if (i != n - 1): 
            print(" + ", end = "")
class Matrix:
    def __init__(self):
        self.size=int(input("Size:"))
    def get_matrix(self):
        self.matrix=[[0 for i in range(self.size)] for j in range(self.size)]
        self.matrix=np.array(self.matrix)
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j]=int(input("Enter:"))
        return self.matrix
    def trace(self):
        self.diagonal=[self.matrix[i][i] for i in range(self.size) ]
        for i in self.diagonal:
            self.trace+=i
        return self.trace
    
