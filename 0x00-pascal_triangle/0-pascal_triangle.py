#!/usr/bin/python3
def pascal_triangle(n):
  """
  Returns a list of lists of integers representing the Pascal's triangle of n.

  Args:
    n: The number of rows in the triangle.

  Returns:
    A list of lists of integers, where each inner list represents a row in the triangle.
  """
 if type(n) is not int:
        raise TypeError("n must be an integer")
    triangle = []
    if n <= 0:
        return triangle
    previous = [1]
    for row_index in range(n):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        triangle.append(rowlist)
    return triangle
