#!/usr/bin/env python3

def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to rotate.

    Returns:
        None. The matrix is edited in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        rotate_2d_matrix(matrix)

        for row in matrix:
            print(row)

        Output:
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)

for row in matrix:
    print(row)

