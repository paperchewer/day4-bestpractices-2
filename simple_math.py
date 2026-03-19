"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    adding the two float variables to return a float variable as the sum of two arguments

    """
    return a+b

def simple_sub(a,b):
    """
    substracting the two float variables to return a float variable as the difference between 
    the first and the second arguments.
    
    """
    return a-b

def simple_mult(a,b):
    """
    multiplying the two float variables to return a float variable as the product of the two arguments
    
    """
    return a*b

def simple_div(a,b):
    """
    dividing the two float variables to return a float variable as the ratio of the  two arguments
    condition: the denominator should be different from zero
    
    """
    return a/b

def poly_first(x, a0, a1):
    """
    calculating a linear function of the float variable x to return a float value
    a0: float, is constant parameter
    a1: float, the slope parameter. 
    
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    calculating a quadratic function of the float variable x to return a float value
    a0: float, is constant parameter
    a1: float, the slope parameter.
    a2: float, the leading parameter 

    """

    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
