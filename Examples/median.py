def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]
    return median

# Test the function
numbers = [10, 5, 15, 7, 20, 3]
result = calculate_median(numbers)
print(result)  # Output: 8.5

print(range(50));

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: Calling function {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("John")

def authenticate(func):
    def wrapper(*args, **kwargs):
        # Add authentication logic here
        if user_authenticated:
            return func(*args, **kwargs)
        else:
            return "Unauthorized"
    return wrapper

@authenticate
def secured_function():
    return "This is a secured function"

# Client call
user_authenticated = True  # Assume user is authenticated
result = secured_function()
print(result)  # Output: "This is a secured function"

user_authenticated = False  # Assume user is not authenticated
result = secured_function()
print(result)  # Output: "Unauthorized"