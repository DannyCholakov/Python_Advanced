n = int(input())
student_records = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in student_records:
        student_records[name] = []
    student_records[name].append(grade)

for student, grades in student_records.items():
    grades_str = " ".join(f"{g:.2f}" for g in grades)
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")
