print("=======for loop=======")

'''For loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
This is less like the for keyword in other programming languages, and works more like 
an iterator method as found in other object-orientated programming languages. 
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

print("========== CLASS REPORT CARD ANALYZER ==========\n")

# ---------- DATA SETUP (using different data types) ----------

# List of Tuples: each tuple = (name, list_of_marks)
students_data = [
    ("Ali", [85, 90, 78]),
    ("Sara", [92, 88, 95]),
    ("Ahmed", [60, 55, 70]),
    ("Hina", [45, 50, 40]),
    ("Bilal", [78, 82, 88])
]

subjects = ("Math", "Science", "English")     # tuple — subject names never change

passed_students = []       # list — will collect names of students who passed
failed_students = []       # list — will collect names of students who failed
grade_summary = {}         # dictionary — will store each student's grade
unique_grades_given = set()  # set — will collect only unique grades assigned

# ---------- MAIN PROCESSING LOOP ----------

for name, marks in students_data:          # unpacking tuple: name (string), marks (list)

    print(f"--- Report for {name} ---")

    total = 0
    subject_count = 0

    # nested for loop: going through each subject's marks using range() + index
    for i in range(len(marks)):
        subject_name = subjects[i]          # accessing tuple by index
        score = marks[i]                    # accessing list by index
        total += score
        subject_count += 1

        # if-elif-else with logical operators to grade EACH subject
        if score >= 90 and score <= 100:
            remark = "Excellent"
        elif score >= 75 and score < 90:
            remark = "Good"
        elif score >= 50 and score < 75:
            remark = "Average"
        else:
            remark = "Needs Improvement"

        print(f"  {subject_name}: {score} -> {remark}")

    average = total / subject_count         # calculate average using loop totals

    # decide overall grade using if-elif-else + logical operators
    if average >= 85 and average <= 100:
        grade = "A"
    elif average >= 70 and average < 85:
        grade = "B"
    elif average >= 50 and average < 70:
        grade = "C"
    else:
        grade = "F"

    grade_summary[name] = grade             # dictionary: storing name -> grade
    unique_grades_given.add(grade)          # set: only unique grades collected

    # logical operator: check pass/fail condition
    if average >= 50 and "F" not in grade:
        passed_students.append(name)
    else:
        failed_students.append(name)

    print(f"  Average: {average:.1f} | Grade: {grade}\n")

# ---------- FINAL SUMMARY (using all collected data structures) ----------

print("========== FINAL SUMMARY ==========")

print("\nPassed students:", passed_students)
print("Failed students:", failed_students)
print("Total passed:", len(passed_students))
print("Total failed:", len(failed_students))

print("\nGrade summary (dictionary):")
for student_name, student_grade in grade_summary.items():
    print(f"  {student_name}: {student_grade}")

print("\nUnique grades given in class (set):", unique_grades_given)

# find the topper using largest-number pattern
topper_name = ""
topper_avg = float('-inf')

for name, marks in students_data:
    avg = sum(marks) / len(marks)
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

print(f"\nClass topper: {topper_name} with average {topper_avg:.1f}")

# count how many students got each grade (frequency pattern using dictionary)
grade_frequency = {}
for student_name, student_grade in grade_summary.items():
    if student_grade in grade_frequency:
        grade_frequency[student_grade] += 1
    else:
        grade_frequency[student_grade] = 1

print("\nHow many students got each grade:")
for grade_letter, count in grade_frequency.items():
    print(f"  Grade {grade_letter}: {count} student(s)")