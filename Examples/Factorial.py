def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def reverse_string(s):
    # Convert the string to a list of characters
    s = list(s)
    # Initialize two pointers, one at the beginning and one at the end
    start = 0
    end = len(s) - 1
    # Swap characters at the start and end pointers until they meet in the middle
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    # Convert the list of characters back to a string
    return ''.join(s)


print(reverse_string("prem"));


def remove_duplicates(lst):
    # Create an empty list to store unique elements
    unique_lst = []
    # Iterate through the original list
    for item in lst:
        # If the item is not already in the unique list, append it
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


list = ["prem", "prem", "prem", "prem"]
print(remove_duplicates(list));

def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    # Reverse the string
    reversed_s = s[::-1]
    # Compare the original and reversed strings
    if s == reversed_s:
        return True
    else:
        return False

print(is_palindrome("aabbaa"));


list11 = ["prem", "prem", "prem", "prem"]
list22 = ["prem", "prem", "prem", "prem"]


print(list(list11,list22))

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print(result)  # Output: 30

exit()
