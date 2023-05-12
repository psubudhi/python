def foo(*args, **kwargs):
    print(args)      # prints tuple of non-keyword arguments
    print(kwargs)    # prints dictionary of keyword arguments

foo(1, 2, 3,4, a='apple', b='banana')

square = lambda x: x**2
print(square(5))  # Output: 25

import copy

list1 = [1, 2, [3, 4]]
list2 = copy.copy(list1)  # Shallow copy

list2[2][0] = 99
print(list1)  # Output: [1, 2, [99, 4]]
print(list2)  #
def foo():
    print("Foo function")

def bar():
    print("Bar function")

if __name__ == "__main__":
    # Code here will only be executed when my_script.py is run directly
    foo()
    bar()

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except Exception:
    print("Error: Division by zero")


    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name}, {self.age} years old"

        def __repr__(self):
            return f"Person('{self.name}', {self.age})"


    person = Person("Alice", 30)

    print(person)  # Output: Alice, 30 years old
    repr_person = repr(person)
    print(repr_person)  # Output: Person('Alice', 30)


    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1


    # Using the generator in a for loop
    for num in count_up_to(5):
        print(num)  # Output: 1, 2, 3, 4, 5