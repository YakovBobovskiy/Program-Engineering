def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open("fib.txt", "w") as file:
    for i, num in enumerate(fib(200), 1):
        file.write(f"{num}\n")