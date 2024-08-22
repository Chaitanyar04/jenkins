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



# # import os
# List1 = [8,9,3,6,1,10]
# List1.reverse()
# print("Reversed list is", List1)

# List2 = [9, 8, 6, 5, 4, 7, 1, 3]
# List2.sort()
# print("sorted list is", List2)

# List3 = []
# List3 = ("List3 =", List3)

# indexvalue = List2[2:6]
# print("index values are", indexvalue)


import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
