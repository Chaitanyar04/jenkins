# def add(x,y):
#     return x+y
#     # print("x + y")

# def subtract(x,y):
#     return x-y
#     # print("x - y")

# def multiply(x,y):
#     return x*y
#     # print("x * y")

# def divide(x,y):
#     return x/y
#     # print("x / y")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
