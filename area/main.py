def areaTriangulo(base, altura):
    '''
    Calculate the area of the triangle
    >>> areaTriangulo(3, 6)
    9.0

    >>> areaTriangulo(9, 3)
    13.5

    >>> areaTriangulo(4, 5)
    8.0
    '''
    return (base*altura)/2

import doctest
doctest.testmod()