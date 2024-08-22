# from ops import *

# def test_add():
#     assert add(3,3) == 6

# def test_subtract():
#     assert subtract(3, 3) == 0

# def test_multiply():
#     assert multiply(4, 3) == 12

# def test_divide():
#     assert divide(15,5) == 3
    

    
from ops import *
import pytest

config = load_config()

def test_add():
    assert add(config['add'][0], config['add'][1]) == 1

def test_subtract():
    assert subtract(config['subtract'][2], config['subtract'][1]) == 1

def test_multiply():
    assert multiply(config['multiply'][1], config['multiply'][1]) == 1

def test_divide():
    assert divide(config['divide'][3], config['divide'][3]) == 1


