def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Usage of the generator function
counter = count_up_to(5)
for num in counter:
    print(num)

import copy

list1 = [1, 2, 3, [4, 5]]
deep_copy = copy.deepcopy(list1)

print(deep_copy is list1)  # False
print(deep_copy[3] is list1[3])  # False
print(deep_copy[3])  # False
print(list1[3])  # False
print(list1)
print(deep_copy)
