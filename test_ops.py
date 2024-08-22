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
    assert add(config['add'][0], config['add'][1]) == 6

def test_subtract():
    assert subtract(config['subtract'][0], config['subtract'][1]) == 0

def test_multiply():
    assert multiply(config['multiply'][0], config['multiply'][1]) == 12

def test_divide():
    assert divide(config['divide'][0], config['divide'][1]) == 3


