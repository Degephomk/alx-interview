#!/usr/bin/python3
def pascal_triangle(n):
  """
  Returns a list of lists of integers representing the Pascal's triangle of n.

  Args:
    n: The number of rows in the triangle.

  Returns:
    A list of lists of integers, where each inner list represents a row in the triangle.
  """

  if n <= 0:
    return []

  triangle = [[1] for _ in range(n)]
  for i in range(1, n):
    for j in range(i + 1):
      if j == 0 or j == i:
        triangle[i].append(1)
      else:
        triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

  return triangle
