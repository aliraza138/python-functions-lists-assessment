
# ============================================
# Class Marks Analyzer
# Assessment: Lists and Loops
# ============================================


# Custom Function 1: Get valid student marks
def get_valid_marks(student_name):

    while True:
        try:
            marks = float(input(f"Enter marks for {student_name} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numeric marks.")


# Custom Function 2: Calculate class average
def calculate_average(student_marks):

    return sum(student_marks) / len(student_marks)


# Custom Function 3: Display highest and lowest scorers
def display_top_and_lowest(student_names, student_marks):

    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    print("\nHighest Marks:", highest_marks)
    print("Highest Scorer(s):")

    for i in range(len(student_marks)):
        if student_marks[i] == highest_marks:
            print(f"{student_names[i]} - {student_marks[i]}")

    print("\nLowest Marks:", lowest_marks)
    print("Lowest Scorer(s):")

    for i in range(len(student_marks)):
        if student_marks[i] == lowest_marks:
            print(f"{student_names[i]} - {student_marks[i]}")


# Main Program
print("=" * 50)
print("             CLASS MARKS ANALYZER")
print("=" * 50)


# Initialize two separate lists
student_names = []
student_marks = []


# Get number of students
while True:
    try:
        total_students = int(input("Enter number of students: "))

        if total_students > 0:
            break
        else:
            print("Please enter at least one student.")

    except ValueError:
        print("Invalid input! Enter a whole number.")


# Collect student names and marks
print("\nEnter Student Details")
print("-" * 50)

for i in range(total_students):

    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ").strip().title()

    while name == "":
        print("Name cannot be empty!")
        name = input("Enter student name: ").strip().title()

    marks = get_valid_marks(name)

    student_names.append(name)
    student_marks.append(marks)


# Calculate class average
class_average = calculate_average(student_marks)


# Count passing and failing students
passing_students = 0
failing_students = 0

for marks in student_marks:

    if marks >= 50:
        passing_students += 1
    else:
        failing_students += 1


# Display class analysis
print("\n")
print("=" * 50)
print("              CLASS PERFORMANCE REPORT")
print("=" * 50)

print(f"Total Students       : {len(student_names)}")
print(f"Class Average        : {class_average:.2f}")

# Display highest and lowest scorers
display_top_and_lowest(student_names, student_marks)


# Display passing and failing students
print("\nPassing Students:", passing_students)
print("Failing Students:", failing_students)


# Display students above class average
print("\nStudents Above Class Average:")
print("-" * 50)

above_average_found = False

for i in range(len(student_marks)):

    if student_marks[i] > class_average:
        print(f"{student_names[i]} - {student_marks[i]:.2f}")
        above_average_found = True

if not above_average_found:
    print("No students scored above the class average.")


# Display marks sorted from highest to lowest
print("\nStudent Marks (Highest to Lowest):")
print("-" * 50)

sorted_marks = sorted(student_marks, reverse=True)

for marks in sorted_marks:
    print(f"{marks:.2f}")


print("=" * 50)
print("         ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)
