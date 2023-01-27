#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """

    sizeBucle = len(matrix[0])
    arrTemp = matrix
    for i in range(sizeBucle):
        for j in range(sizeBucle):
            arrTemp[i][j] = matrix[j][i]
