def fib(n):
    fib1 = fib2 = 1
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib_sum