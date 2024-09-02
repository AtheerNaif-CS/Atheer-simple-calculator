def add(x,z):
    return x+z
def subtract(x,z):
    return x-z
def multiply():
    return x*z 
def devide(x,z):
    if z==0 :
        return "Invalid value for denominator, cant't divide by 0!"
    return x/z
def square(x):
    return x**2
def power(x,z):
    return x**z 
def square_root(x):
    return X**0.5 


def test_add():
    assert add(5,4) == 9
    assert add(-3,6) == 3

def test_subtract():
    assert subtract(5,4) == 1
    assert subtract(-3,6) == -9

def test_multiply():
    assert multiply(5,4) == 20
    assert multiply(-3,6) == -18

def test_devide():
    assert devide(10,5) == 2
    assert devide(8,2) == 4

def test_square():
    assert square(3) == 9
    assert square(4) == 16

def test_power():
    assert power(2,3) == 8
    assert power(3,2) == 9

def test_square_root():
    assert square_root(9) == 3
    assert add(81) == 9


print(add(7,6))

