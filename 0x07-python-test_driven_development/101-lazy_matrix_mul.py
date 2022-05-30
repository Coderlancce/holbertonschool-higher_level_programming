#!/usr/bin/python3
import numpy as np
"""
The math operations module 4
============================
this module has an lazy_matrix_mul fucn just for now
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Funtion that multiplies 2 matrix with numpy.
    """
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return m_a.dot(m_b)
