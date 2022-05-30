#!/usr/bin/python3
"""
Module multiplies 2 matrices
"""


def test(matrix, buff, err, msg):
    """ 
    Test m_a and m_b matrix 
    """
    try:
        errMatrix = buff.index(False)
    except ValueError:
        return
    else:
        raise err(msg.format(matrix[errMatrix]))

def mulVec(vec1, vec2):
    """ 
    Escalar vectors multiplication, returns result 
    """
    return sum(x * y for x, y in zip(vec1, vec2))

def matrix_mul(m_a, m_b):
    """
    Function to mul two matrices
    """

    inp = [m_a, m_b]
    inpTxt = ["m_a", "m_b"]

    check = [type(x) is list for x in inp]
    test(inpTxt, check, TypeError, "{} must be a list")

    check = [all(type(x) == list for x in y) for y in inp]
    test(inpTxt, check, TypeError, "{} must be a list of lists")

    check = [y != [] and all(x != [] for x in y) for y in inp]
    test(inpTxt, check, ValueError, "{} can't be empty")

    check = [all(all(type(z) is int or type(z) is float for z in y) for y in x)
             for x in inp]
    test(inpTxt, check, TypeError, "{} should contain only integers or floats")

    check = [all(len(y) == len(x[0]) for y in x) for x in inp]
    test(inpTxt, check, TypeError, "each row of {} must be of the same size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    xAxis = len(m_b[0])
    yAxis = len(m_a)

    return [[mulVec(m_a[y], [m_b[i][x] for i in range(xAxis)])
             for x in range(xAxis)] for y in range(yAxis)]
