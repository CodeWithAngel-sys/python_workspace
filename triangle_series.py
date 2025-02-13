import math

try:
    input_N = int(input('Enter the value of N: '))
    n = input_N
    sum = 0

    for i in range(1, n+1):
        sum += i
        print(sum, end=' ')
except ValueError:
    print("Invalid input. Please enter an integer.")
 
    