import math

input_N = int(input("Enter the value of N: "))

def math_factorial():
    for n in range(input_N):
        catalan = math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
        print(catalan)

math_factorial()