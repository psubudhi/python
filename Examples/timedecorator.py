import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    # Some time-consuming operation
    time.sleep(2)
    return "Function executed"
result = slow_function()
print(result)  # Output: "Function executed"


def caching_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = hash(str(args) + str(kwargs))
        if key in cache:
            print(f"Returning cached result for {func.__name__} with key {key}")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

@caching_decorator
def expensive_operation(n):
    # Some expensive operation
    return n * n

result = expensive_operation(5)
print(result)  # Output: "Function executed"
