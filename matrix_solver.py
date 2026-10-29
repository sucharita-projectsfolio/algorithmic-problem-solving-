def matrix_vector_multiply(matrix, vector):
    if not matrix or not vector or len(matrix[0]) != len(vector):
        raise ValueError("Invalid dimensions for matrix-vector multiplication.")
    return [round(sum(r * v for r, v in zip(row, vector)), 4) for row in matrix]

if __name__ == "__main__":
    A = [[1.5, 2.0, 0.0], [0.0, 3.2, 1.1], [4.0, 0.5, 2.3]]
    x = [2.0, 1.0, 3.0]
    print("Output:", matrix_vector_multiply(A, x))
