import numpy as np
print("Enter 1st 2x2 matrix rows (each row 2 numbers separated by space):")
mat1 = np.array([list(map(int, input().split())) for _ in range(2)])
print("Enter 2nd 2x2 matrix rows (each row 2 numbers separated by space):")
mat2 = np.array([list(map(int, input().split())) for _ in range(2)])
print("Sum of matrices:")
print(np.add(mat1, mat2))
