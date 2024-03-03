import numpy as np

def make_diagonally_dominant(A, b):
    n = len(b)
    for i in range(n):
        max_val = abs(A[i, i])
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > max_val:
                max_val = abs(A[j, i])
                max_row = j
        
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]
    
    return A, b

def gauss_seidel(A, b, x0, eps):
    n = len(b)
    x = x0.copy()
    iteration = 0
    print()
    while True:
        x_new = np.zeros(n)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        iteration+=1
        print("Iteration ", iteration, ":", x_new)
        if np.linalg.norm(x - x_new) < eps:
            break
        
        x = x_new.copy()
    
    return x, iteration


# Дані матриці A та вектора b
A = np.array([
    [0.341, -0.542, 0.418, -2.110],
    [-0.111, 0.915, 0.012, 0.341],
    [0.546, 0.211, -0.318, 1.810],
    [0.302, 0.201, 2.130, -0.115]
])

b = np.array([-1.893, 2.249, 2.249, 2.518])

x0 = [1, 1, 1, 1]

eps1 = 0.01
eps2 = 0.0001

print(A, b)
A_transformed, b_transformed = make_diagonally_dominant(A, b)
print()
print(A_transformed, b_transformed)

solution_eps1, iterations_eps1 = gauss_seidel(A_transformed, b_transformed, x0, eps1)
print(f"Solution for eps1 = {solution_eps1}")
print(f"Number of iterations to achieve accuracy eps1 = {eps1}: {iterations_eps1}")

solution_eps2, iterations_eps2 = gauss_seidel(A_transformed, b_transformed, x0, eps2)
print(f"\nSolution for eps2 = {solution_eps2}")
print(f"Number of iterations to achieve accuracy eps2 = {eps2}: {iterations_eps2}")
