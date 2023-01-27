#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """

    sizeBucle = len(matrix[0])
    arrTemp = []
    count = 0
    for i in range(sizeBucle):
        for j in range(sizeBucle):
            arrTemp.append(matrix[sizeBucle-1][i])
            # print("{}-{}".format((sizeBucle-1),i))
            # print(matrix[sizeBucle-1][i])
            sizeBucle = sizeBucle-1
        sizeBucle = len(matrix[0])

    for row in range(sizeBucle):
        for col in range(sizeBucle):
            matrix[row][col] = arrTemp[count]
            count += 1
