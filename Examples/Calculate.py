def calculate_average_grade(students):
    total_grades = 0
    num_students = len(students)
    for student in students:
        total_grades += student['grade']
    average_grade = total_grades / num_students
    return average_grade

# Test the function
students = [{'name': 'Alice', 'grade': 85},
            {'name': 'Bob', 'grade': 90},
            {'name': 'Charlie', 'grade': 78},
            {'name': 'Dave', 'grade': 92}]
result = calculate_average_grade(students)
print(result)  # Output: 86.25
