from typing import List, Any, Union


def fibw(n):
    a, b = 0, 1;
    while (a < n):
        print(a, end=",");
        a, b = b, a + b;
    print()

def fiba(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
