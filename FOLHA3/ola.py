def funcaoqualquer(matriz, escalar):
    """
    Multiplies each element of a matrix by a given scalar.
    This function takes a 2D list (matrix) and a scalar value as input, and multiplies
    each element of the matrix by the scalar. The operation is performed in-place, 
    modifying the original matrix.
    Args:
        matriz (list of list of float): A 2D list representing the matrix to be scaled.
        escalar (float): The scalar value by which to multiply each element of the matrix.
    Returns:
        list of list of float: The modified matrix after scaling.
    Example:
        >>> matriz = [[1, 2], [3, 4]]
        >>> escalar = 2
        >>> funcaoqualquer(matriz, escalar)
        [[2, 4], [6, 8]]
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] *= escalar

    return matriz

