import numpy as np
print("Enter 2x2 matrix rows (each row 2 numbers separated by space):")
mat = np.array([list(map(int, input().split())) for _ in range(2)])
print("Transpose of matrix:")
print(np.transpose(mat))
