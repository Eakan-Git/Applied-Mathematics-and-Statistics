import numpy as np
from scipy.linalg import qr
from sympy import Matrix
print("Phan ra QR:")
A = np.array([[1, 1, 1], [2, 1, 2], [3, 2, 2], [4, 2, 1]])
print("A =\n", A, end="\n\n")
Q, R = qr(A)
print("Q =\n", Q, end='\n\n')
print("R =\n", R)


print("\n\nCheo hoa ma tran:")
A = Matrix([[1, 3], [5, -4]])
print("A =", A, end="\n\n")
P, D = A.diagonalize()
print("P = ", P.evalf(3))
print("\n\nP_inv = ", P.inv().evalf(3))
print("\n\nD = ", D.evalf(3))
if A.is_diagonalizable():
	print("\nMa tran cheo hoa duoc.")
else:
	print("\nMa tran khong cheo hoa duoc.")