import numpy as np

# 1 -2 3 9
# -1 3 -1 -6
# 2 -5 5 17
print("Vi du 1:")
print("x - 2y + 3z = 9")
print("-x + 3y - z = -6")
print("2x -5y + 5z = 17")
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])
X = np.linalg.solve(A,B)
print("Dap an vi du 1: ", X)

# 1 -3 1 4
# 2 -8 8 -2
# -6 3 -15 9
print("\nVi du 2:")
print("x - 3y + z = 4")
print("2x - 8y + 8z = -2")
print("-6x + 3y - 15z = 9")
A = np.array([[1, -3, 1], [2, -8, 8], [-6, 3, -15]])
B = np.array([4, -2, 9])
X = np.linalg.solve(A,B)
print("Dap an vi du 2: ", X)

# 1 -1 1 8
# 2 3 -1 -2
# 3 -2 -9 9
print("\nAp dung 1:")
print("x - y + z = 8")
print("2x + 3y - z = -2")
print("3x - 2y - 15z = 9")
A = np.array([[1, -1, 1], [2, 3, -1], [3, -2, -9]])
B = np.array([8, -2, 9])
X = np.linalg.solve(A,B)
print("Dap an ap dung 1: ", X)


# 3 2 1 1 -2
# 1 -1 4 -1 -1
# -2 -2 -3 1 9
# 1 5 -1 2 4
print("\nAp dung 2:")
print("3x + 2y + z + t = -2")
print("x - y + 4z -t = -1")
print("-2x - 2y - 3z + t = 9")
print("x + 5y - z + 2t = 4")
A = np.array([[3, 2, 1, 1], [1, -1, 4, -1], [-2, -2, -3, 1], [1, 5, -1, 2]])
B = np.array([-2, -1, 9, 4])
X = np.linalg.solve(A,B)
print("Dap an ap dung 2: ", X)