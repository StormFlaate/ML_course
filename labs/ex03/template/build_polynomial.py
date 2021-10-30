# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""

    poly_list = np.ones(degree)
    for index, j in enumerate(poly_list):
        poly_list[index] = x**index

    return poly_list
