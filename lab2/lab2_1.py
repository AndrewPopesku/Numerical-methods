import numpy as np

def gauss_elimination(A, f):
    n = len(A)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        x[i] = f[i] / A[i][i]
        print(x)
        for j in range(i):
            factor = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= factor * A[i][k]
            f[j] -= factor * f[i]

            print("Матриця A:")
            print(A)
            print()

    return x

A = np.array([[0.13, -0.08, -0.18, 0.13],
              [0.11, -0.1, -0.06, 0.21],
              [0.09, 0, -0.08, 0.03],
              [0.09, -0.06, -0.16, 0.29]])

f = np.array([0.25, 0.13, 0.13, 0.63])

x = gauss_elimination(A, f)
print("Розв'язок СЛАР методом Гауса (правий верхній кут, схема єдиного ділення):", x)
