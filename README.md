# Python Functions and Lists Assessment

## Project Overview

This repository contains two Python programs developed as part of
Assessment Set 2. The project focuses on practical implementation of
Python functions, string manipulation, lists, loops, input validation,
and basic data analysis.

Both programs demonstrate how Python concepts can be used to solve
academic problems through structured and reusable code.

## Project Programs

### Task 1: Student Result Card Generator

**File:** `student_result_card.py`

This program generates an individual student's result card based on
marks obtained in five subjects.

**Key Features:** - Takes the student's name and roll number as input. -
Collects marks in five subjects. - Validates marks between 0 and 100. -
Validates the roll number using the `isdigit()` method. - Formats the
student's name using `strip()` and `title()`. - Calculates total marks
and overall percentage. - Assigns grades according to the given grading
criteria. - Declares the final result as Fail if any subject mark is
below 40. - Displays a formatted result card using f-strings.

### Task 2: Class Marks Analyzer

**File:** `class_marks_analyzer.py`

This program analyzes the academic performance of an entire class using
Python lists and loops.

**Key Features:** - Takes the total number of students as input. -
Stores student names and marks in separate lists. - Uses `append()` to
store student information. - Validates marks between 0 and 100. -
Calculates the class average. - Identifies students with the highest and
lowest marks. - Counts passing and failing students. - Displays students
who scored above the class average. - Sorts student marks from highest
to lowest.

## Python Concepts and Functions Used

### Task 1: Functions and Strings

  Concept / Function         Purpose
  -------------------------- ------------------------------------------------------
  `def`                      Defines reusable functions.
  `return`                   Returns values from functions.
  `get_valid_marks()`        Accepts and validates subject marks.
  `calculate_percentage()`   Calculates the overall percentage.
  `get_grade()`              Determines the letter grade.
  `format_name()`            Cleans and formats the student's name.
  `isdigit()`                Checks whether the roll number contains digits only.
  `strip()`                  Removes unnecessary spaces from the name.
  `title()`                  Capitalizes the first letter of each word.
  f-strings                  Displays formatted result information.
  `if-elif-else`             Applies grading and result conditions.
  `try-except`               Handles invalid numeric input.

### Task 2: Lists and Loops

  Concept / Function     Purpose
  ---------------------- -------------------------------------------------------
  `student_names = []`   Stores student names.
  `student_marks = []`   Stores student marks.
  `append()`             Adds student information to lists.
  `len()`                Counts the number of students.
  `sum()`                Calculates the total marks.
  `max()`                Finds the highest marks.
  `min()`                Finds the lowest marks.
  `sorted()`             Sorts marks in descending order using `reverse=True`.
  `for` loop             Iterates through student records.
  `while` loop           Repeats input until valid data is entered.
  Custom functions       Organize calculations and repeated operations.
  `if-else`              Counts passing and failing students.

## How to Run the Programs

### Requirements

-   Python 3.x
-   Visual Studio Code (recommended)
-   Python extension for VS Code (recommended)

### Running Task 1: Student Result Card Generator

1.  Open the project folder in VS Code.
2.  Open the integrated terminal.
3.  Run:

``` bash
python student_result_card.py
```

### Running Task 2: Class Marks Analyzer

Run the following command in the VS Code terminal:

``` bash
python class_marks_analyzer.py
```

**Note:** On Windows, the `py` launcher can also be used instead of
`python`:

``` bash
py student_result_card.py
py class_marks_analyzer.py
```

## Sample Input and Output

### Task 1: Student Result Card Generator

**Sample Input:**

``` text
Enter Student Name: Ali Raza
Enter Roll Number: 138
Enter marks for English (0-100): 85
Enter marks for Mathematics (0-100): 90
Enter marks for Computer Science (0-100): 88
Enter marks for Physics (0-100): 75
Enter marks for Chemistry (0-100): 92
```

**Sample Output:**

``` text
STUDENT RESULT CARD

Student Name      : Ali Raza
Roll Number       : 138

English           : 85.00
Mathematics       : 90.00
Computer Science  : 88.00
Physics           : 75.00
Chemistry         : 92.00

Total Obtained    : 430.00 / 500
Overall Percentage: 86.00%
Letter Grade      : A
Final Status      : Pass
```

### Task 2: Class Marks Analyzer

**Sample Input:**

``` text
Enter number of students: 5

Student 1
Enter student name: Ali
Enter marks for Ali (0-100): 85

Student 2
Enter student name: Ahmed
Enter marks for Ahmed (0-100): 92

Student 3
Enter student name: Sara
Enter marks for Sara (0-100): 78

Student 4
Enter student name: Ayesha
Enter marks for Ayesha (0-100): 95

Student 5
Enter student name: Usman
Enter marks for Usman (0-100): 40
```

**Sample Output:**

``` text
CLASS PERFORMANCE REPORT

Total Students       : 5
Class Average        : 78.00

Highest Marks: 95.0
Highest Scorer(s):
Ayesha - 95.0

Lowest Marks: 40.0
Lowest Scorer(s):
Usman - 40.0

Passing Students: 4
Failing Students: 1

Students Above Class Average:
Ali - 85.00
Ahmed - 92.00
Ayesha - 95.00

Student Marks (Highest to Lowest):
95.00
92.00
85.00
78.00
40.00
```

## Project Structure

``` text
Python-Assessment-Set-2/
|
|-- student_result_card.py
|-- class_marks_analyzer.py
|-- README.md
```

## Learning Outcomes

Through this assessment, I practiced:

-   Creating and using custom Python functions.
-   Working with function parameters and return values.
-   Manipulating and formatting strings.
-   Creating and managing Python lists.
-   Using built-in functions for calculations and sorting.
-   Implementing loops and conditional statements.
-   Validating user input and handling errors.
-   Generating structured output using f-strings.

## Conclusion

This assessment helped strengthen my understanding of Python
fundamentals through two practical programs. Both tasks demonstrate the
application of functions, strings, lists, loops, and input validation in
solving academic problems.

