# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:53:18 2022

@author: Rohan
"""
import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x <= y:
        return x * y
    else:
        return x / y

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    f = np.vectorize(scalar_function)
    return f(x, y)
