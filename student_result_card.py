
# ============================================
# Student Result Card Generator
# Assessment: Functions, Strings and Lists
# ============================================


# Function 1: Get valid marks from the user
def get_valid_marks(subject):

    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numeric marks.")


# Function 2: Calculate overall percentage
def calculate_percentage(total, max_total):

    percentage = (total / max_total) * 100
    return percentage


# Function 3: Calculate grade based on percentage
def get_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Function 4: Format student's name
def format_name(name):

    return name.strip().title()


# Main Program
print("=" * 45)
print("       STUDENT RESULT CARD GENERATOR")
print("=" * 45)


# Get student name
student_name = format_name(input("Enter Student Name: "))


# Get valid roll number
while True:
    roll_number = input("Enter Roll Number: ").strip()

    if roll_number.isdigit():
        break
    else:
        print("Invalid Roll Number! Digits only are allowed.")


# List of five subjects
subjects = [
    "English",
    "Mathematics",
    "Computer Science",
    "Physics",
    "Chemistry"
]


# Store subject marks in a dictionary
marks_obtained = {}

for subject in subjects:
    marks_obtained[subject] = get_valid_marks(subject)


# Calculate total marks
total_marks = sum(marks_obtained.values())

# Maximum marks
max_total = len(subjects) * 100


# Calculate percentage
percentage = calculate_percentage(total_marks, max_total)


# Calculate grade
grade = get_grade(percentage)


# Check if any subject marks are below 40
if any(mark < 40 for mark in marks_obtained.values()):
    final_status = "Fail"
    grade = "Fail"
else:
    final_status = "Pass"


# Display Result Card
print("\n")
print("=" * 45)
print("              STUDENT RESULT CARD")
print("=" * 45)

print(f"Student Name      : {student_name}")
print(f"Roll Number       : {roll_number}")

print("-" * 45)
print("SUBJECTS              OBTAINED MARKS")
print("-" * 45)

for subject, marks in marks_obtained.items():
    print(f"{subject:<22} {marks:>10.2f}")

print("-" * 45)

print(f"Total Obtained    : {total_marks:.2f} / {max_total}")
print(f"Overall Percentage: {percentage:.2f}%")
print(f"Letter Grade      : {grade}")
print(f"Final Status      : {final_status}")

print("=" * 45)
print("           RESULT GENERATED SUCCESSFULLY")
print("=" * 45)
