def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
fibonacci = list(fib(n))[-1]
print(fibonacci)