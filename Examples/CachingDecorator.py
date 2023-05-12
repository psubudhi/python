def caching_decorator(func):
    cache = {}  # Create an empty dictionary to store cached results

    def wrapper(*args, **kwargs):
        # Define a wrapper function that takes any number of positional and keyword arguments
        key = tuple(args) + tuple(sorted(kwargs.items()))  # Create a unique key for caching based on input arguments
        if key not in cache:  # Check if the result for the given arguments is already in the cache
            cache[key] = func(*args, **kwargs)  # If not, calculate the result using the decorated function and store it in the cache
        return cache[key]  # Return the cached result

    return wrapper  # Return the wrapper function as the actual decorated function

@caching_decorator
def expensive_function(arg1, arg2):
    # Some expensive operation
    print(f"Calculating result for ({arg1}, {arg2})")
    return arg1 + arg2

# Define the expensive_function and apply the caching_decorator to it using the @ syntax

result1 = expensive_function(2, 3)  # Call the expensive_function with arguments 2 and 3
# Output: Calculating result for (2, 3)
print(result1)  # Output: 5 (result of the expensive_function)

result2 = expensive_function(3,2)  # Call the expensive_function again with the same arguments
# Output: (no output, cached result used)
print(result2)  # Output: 5 (cached result used, no re-calculation)

result3 = expensive_function(4, 5)  # Call the expensive_function with different arguments 4 and 5
# Output: Calculating result for (4, 5)
print(result3)  # Outpu
