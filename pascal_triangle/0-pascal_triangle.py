#!/usr/bin/python3
"""
Function that returns a list of lists of integers 
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns  Pascal’s triangle"""

    triangle = []
    row = []
    previous = []
  
  for i in range(0, n + 1):
      row = [j > 0 and j < i - 1 and i > 2 and previous[j-1] + previous[j] or 1 for j in range(0, i)]
    prev_row = row
    triangle += [row]
  
  return triangle[1:]
