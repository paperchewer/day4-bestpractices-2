from simple_math import simple_add, simple_sub, simple_mult, simple_div, poly_first, poly_second 

def test_simple_add(): 
    assert simple_add(2,3) == 5
    assert simple_add(0,0) == 0
    assert simple_add(-1, 1) == 0 

def test_simple_sub():
    assert simple_sub(5, 3) == 2
    assert simple_sub(0, 0) == 0
    assert simple_sub(-1, -1) == 0

def test_simple_mult():
    assert simple_mult(3, 4) == 12
    assert simple_mult(0, 5) == 0
    assert simple_mult(-2, 3) == -6

def test_simple_div():
    assert simple_div(10, 2) == 5
    assert simple_div(0, 5) == 0
    assert simple_div(-6, 2) == -3

def test_poly_first():
    assert poly_first(2, 0, 1) == 2    # 0 + 1*2 = 2
    assert poly_first(0, 5, 3) == 5    # 5 + 3*0 = 5
    assert poly_first(3, 1, 2) == 7    # 1 + 2*3 = 7

def test_poly_second():
    assert poly_second(2, 0, 0, 1) == 4   # 0 + 0*2 + 1*(2**2) = 4
    assert poly_second(0, 5, 3, 2) == 5   # 5 + 3*0 + 2*(0**2) = 5
    assert poly_second(3, 1, 2, 1) == 16  # 1 + 2*3 + 1*(3**2) = 16
