#!/usr/bin/python3
"""Defines a function that multiplies two matrices using NumPy.

Provides ``lazy_matrix_mul``, a thin wrapper around
``numpy.matmul`` that lets NumPy validate the inputs and raise its
own errors for invalid matrices.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list): The left-hand matrix.
        m_b (list): The right-hand matrix.

    Returns:
        numpy.ndarray: The matrix product of ``m_a`` and ``m_b``.
    """
    return np.matmul(m_a, m_b)
