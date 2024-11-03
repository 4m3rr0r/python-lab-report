def calculate_gpa(grades):
    total_points = 0
    for grade in grades:
        if grade >= 90:
            total_points += 4.0
        elif grade >= 80:
            total_points += 3.0
        elif grade >= 70:
            total_points += 2.0
        elif grade >= 60:
            total_points += 1.0
        else:
            total_points += 0.0
            
    return total_points / len(grades)

gpa_list = []
for i in range(10):
    grades = []
    print(f"Enter grades for student {i + 1}:")
    for j in range(5): 
        grade = float(input(f"Grade for subject {j + 1}: "))
        grades.append(grade)
    gpa = calculate_gpa(grades)
    gpa_list.append(gpa)
    print(f"GPA for student {i + 1}: {gpa:.2f}\n")

print("All GPAs:")
for i, gpa in enumerate(gpa_list):
    print(f"Student {i + 1}: {gpa:.2f}")
