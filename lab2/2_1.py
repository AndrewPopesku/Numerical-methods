import numpy as np

def gaussian(A, b):
    A = np.hstack((A, b))
    n = A.shape[0]

    for i in range(n):
        A[i] /= A[i][n-1-i]
        for j in range(i+1, n):
            A[j] -= A[i] * A[j][n-1-i]

        print(A)
        print()
    
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = A[i][-1]
        for j in range(n-1, i, -1):
            X[i] -= A[i][n-1-j] * X[j]

    return X


if __name__ == "__main__":
    A = np.array([[0.13, -0.08, -0.18, 0.13],
                  [0.11, -0.1, -0.06, 0.21],
                  [0.09, 0, -0.08, 0.03],
                  [0.09, -0.06, -0.16, 0.29]])

    f = np.array([[0.25],
                  [0.13],
                  [0.13],
                  [0.63]])

    solution = gaussian(A, f)
    print("Computed Solution:", solution)
