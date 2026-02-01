# def fibonacci_series(n):
#     fib = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib.append(a)
#         a, b = b, a + b
#     return fib

# n = 10  
# print("Fibonacci series:", fibonacci_series(n))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate Fibonacci series up to n terms
def fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=' ')

# Example usage
n = 10
print("Fibonacci series:")
fibonacci_series(n)

