# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    w = np.linalg.lstsq(tx,y)[0]
    N = y.shape[0] # Number of elements in vector y
    error = y-(tx@w)
    loss = (1/(2*N))*(error.T @ error)
    return w, loss
