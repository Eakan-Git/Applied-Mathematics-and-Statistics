def read_file(file_name_in):
	matrix = []
	with open(file_name_in, 'r') as f:
		for line in f:
			line = line.strip()
			if len(line) > 0:
				matrix.append(list(map(int, line.split())))
	f.close()
	return matrix

def print_matrix(matrix):
	if matrix == None:
		print(None)
		return
	for row in matrix:
		print(*row)
#create a brand new zero matrix
def zeros_matrix(rows, cols):
	matrix = []
	while len(matrix) < rows:
		matrix.append([])
		while len(matrix[-1]) < cols:
			matrix[-1].append(0.0)
	return matrix

#copy a matrix
def copy_matrix(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	cop = zeros_matrix(rows, cols)
	for i in range(rows):
		for j in range(cols):
			cop[i][j] = matrix[i][j]
	return cop
def det(matrix):
	total = 0
	indices = list(range(len(matrix)))
	#if 2x2 matrix then
	if len(matrix) == 2 and len(matrix[0]) == 2:
		val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
		return val
	for i in indices: 
		#find sub matrix
		tmpMatrix = copy_matrix(matrix)
		#remove the 1st row
		tmpMatrix = tmpMatrix[1:]
		height = len(tmpMatrix)
		for j in range(height):
			#for each remaining row of submatrix
			#remove column elements
			tmpMatrix[j] = tmpMatrix[j][0:i] + tmpMatrix[j][i+1:]

		sign = (-1)**(i%2)
		sub_det = calc_determinant_row_operation(tmpMatrix)
		total += sign * matrix[0][i] * sub_det
	return total
def calc_determinant_row_operation(matrix):
	if len(matrix) == len(matrix[0]):
		res = det(matrix)
		return res
	else:
		return None

def transpose(A):
	m, n = len(A), len(A[0])
	return [[A[i][j] for i in range(m)] for j in range(n)]

def multiply_scalar_matrix(scalar, A_list):
    return [[scalar * a for a in a_row] for a_row in A_list]

def create_submatrix(A, i_row, i_col):
    sub_A = copy_matrix(A)
    
    #Delete row
    sub_A = sub_A[:i_row] + sub_A[i_row+1:]
    
    #Delete col
    n_row_sub = len(sub_A)
    for i in range(n_row_sub): 
        sub_A[i] = sub_A[i][:i_col] + sub_A[i][i_col+1:]
    return sub_A
def invert_matrix_row_operation(A):
	rows = len(A)
	cols = len(A[0])
	if rows != cols:
		print("Not a square matrix.")
		return None
	det = calc_determinant_row_operation(A)
	if det == 0:
		print("Matrix irreversible.")
		return None
	res = zeros_matrix(rows, cols)
	trans = transpose(A)
	for i in range(rows):
		for j in range(cols):
			submatrix = create_submatrix(trans, i, j)
			sign = (-1)**(i+j)
			res[i][j] = sign * calc_determinant_row_operation(submatrix)
	res = multiply_scalar_matrix(1/det, res)
	return res

def write_file(file_name_out, det, inv_mat):
	with open(file_name_out, 'w') as f:
		if det == None:
			f.write("Not a square matrix.")
		else:
			f.write("Det: " + str(det) + '\n')
			f.write("Inverse matrix:\n")
			if det == 0:
				f.write(str(None))
			else:
				for row in inv_mat:
					f.write(' '.join([str(a) for a in row]) + '\n')
		f.close()

def main():
	matrix = read_file('input.txt')
	print("Given matrix:")
	print_matrix(matrix)
	det = calc_determinant_row_operation(matrix)
	print("Det:", det)
	inv_mat = invert_matrix_row_operation(matrix)
	print("Inverse matrix: ")
	print_matrix(inv_mat)
	write_file('19127608_output.txt', det, inv_mat)
main()