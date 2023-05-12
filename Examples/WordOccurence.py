def count_string_occurrences(strings):
    occurrences = {}
    for string in strings:
        if string in occurrences:
            occurrences[string] += 1
        else:
            occurrences[string] = 1
    return occurrences

# Test the function
strings = []

#strings = ["apple", "orange", "banana", "apple", "orange", "orange"]
result = count_string_occurrences(strings)
print(result)  # Output: {'apple': 2, 'orange

