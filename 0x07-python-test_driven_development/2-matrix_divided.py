#!/usr/bin/python3
""" Module for the matrix_divided method. """


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix: Divided matrix.
        div: Number to divide the matrix by.

    Returns:
        A new matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If the rows of the matrix have different sizes.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div equals to 0.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(n / div, 2) for n in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
