def nth_term_of_triangle_series(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    return n * (n + 1) // 2


input_n = int(input("Enter a positive integer: "))
n = input_n
print(f"The {n}th term of the triangle series is: {nth_term_of_triangle_series(n)}")