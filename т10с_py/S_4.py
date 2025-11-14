import time


class SimpleTimer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__}{args} = {result} | Время: {end - start:.3f} сек")
        return result


@SimpleTimer
def sum_numbers(n):
    return sum(range(n + 1))


@SimpleTimer
def multiply(a, b):
    return a * b


print("Результаты:")
multiply(15, 20)
sum_numbers(100)