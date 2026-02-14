def strongNumber(n):
    import math

    n = 145
    temp = n
    s = 0

    while n:
        s += math.factorial(n % 10)
        n //= 10

    print("Strong" if s == temp else "Not Strong")