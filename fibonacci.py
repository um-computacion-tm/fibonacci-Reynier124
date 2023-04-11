import unittest
#Recursiva
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

'''
iterativa
def fibonacii(number):
    fibonacci_numbers = [0 , 1]
    total = 1
    for index in range(2, number + 1):
        total = fibonacci[-2] + fibonacci[-1]
        fibonacci_numbers.append(total)
    return total
'''