def find_largest_and_smallest(numbers):
    if not numbers:
        return None
    largest = smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

# Test the function
numbers = [10, 2, 45, 100, -5, 30]
result = find_largest_and_smallest(numbers)
print(result)  # Output: (100, -5)
