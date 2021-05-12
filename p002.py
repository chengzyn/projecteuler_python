# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:50:56 2020

@author: Nicholas
"""
# Note that this problem defines first two terms as 1 and 2
import timeit


# Function for nth fibonacci number - using Recursion
def Fibo1(n):
    if n < -1:
        return None
    elif n == -1:
        return 0
    elif n == 0:
        return 1
    else:
        return Fibo1(n - 1) + Fibo1(n - 2)


# Function for nth fibonacci number - Dynamic Programming
FibArray = [0, 1]


def Fibo2(n):
    n += 2  # This line is required to conform to the question definitions
    if n < 0:
        return None
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

    # Function for nth fibonacci number - Space Optimisataion


def Fibo3(n):
    n += 2  # This line is required to conform to the question definitions
    a = 0
    b = 1
    if n < 0:
        return None
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

    # Driver function


def main(Fibo):
    total = 0
    n = 1
    while Fibo(n) < 4000000:
        if Fibo(n) % 2 == 0:
            total += Fibo(n)
        n += 1
    return total


# Do a test for times

# print("Recursive Fibonacci took", timeit.timeit('RunTest(Fibo1)', number=1, globals=globals()), "seconds")
# print("Dynamic programming Fibonacci took", timeit.timeit('RunTest(Fibo2)', number=1, globals=globals()), "seconds")
# print("Space optimized Fibonacci took", timeit.timeit('RunTest(Fibo3)', number=1, globals=globals()), "seconds")

if __name__ == '__main__':
    print(main(Fibo3))
