# Student Learning Portal

**Module:** PROG211 – Object-Oriented Programming 1  
**Institution:** Limkokwing University, Sierra Leone  
**Domain:** Education

## Project overview
This small console-based Python project demonstrates how a learning portal can create courses, register students, update student records and enroll students in courses. It is an educational prototype, not a production student information system.

## Requirements
- Python 3.7 or newer (no third-party packages required).

## Running the program
1. Save `student_learning_portal.py` to your computer.
2. Open a terminal in the folder containing the file.
3. Run `python student_learning_portal.py` (or `python3 student_learning_portal.py`).

The script runs a demonstration with two courses and two students. It does not provide an interactive menu or save data between runs.

## OOP features
- `Course`: course code, name, credits and learning level; instance method `display_info()`, class method `get_total_courses()`, static method `is_valid_course_code()`.
- `Student`: student ID, name, age, campus and one enrolled course; instance methods `display_info()`, `update_record()`, `enroll()`; class method `get_total_students()`; static methods `is_valid_id()`, `is_valid_age()`.
- Object interaction: a `Student` object enrolls in a `Course` object.

## Data structures
- **List:** `learning_portal` stores registered `Student` objects; `add_student()` checks for duplicate IDs and `display_all_students()` displays them.
- **Optional tuples:** `CAMPUSES` and `LEVELS` provide fixed choices used to validate campus and course level.

## Digital Public Goods (DPG) alignment
- **Open-source:** The source can be published in a public GitHub repository. Choose and include an appropriate open-source `LICENSE` file before claiming the repository is openly licensed.
- **Inclusive:** The program runs in a text-based terminal without paid packages; this can be useful in lower-resource settings. Accessibility across devices and assistive technologies has not been tested.
- **Privacy-respecting:** The demo does not collect phone numbers, addresses or national IDs. It does handle student names, IDs and ages; use fictional sample records and do not upload real student data. It has no authentication or persistent storage and is not ready for real-world deployment.
- **Modular and reusable:** Course and Student responsibilities are separated into classes, with additional functions for list management.

## Limitations
- Each student can be enrolled in only one course at a time.
- Data is held in memory and is lost when the program stops.
- The demonstration uses pre-defined records; there is no interactive input menu.
- Validation is basic and does not replace production security controls.
