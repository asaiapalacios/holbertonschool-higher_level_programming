'''
Write a function fibonacci(x): computes fibonacci number of the parameter
'''

#Using loop technique
def fibonacci(x):
    a, b = 1, 1
    for i in range (x-1):
        a, b = b, a+b
    return a
'''
Version 2
def fibonacce(x):
    if x < 2:
        return x
    return fibonacci(x-2) + fibonacci(x-1)
'''
    
