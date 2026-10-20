"""PROG211: Student Learning Portal (Education domain).
A simple, console-based demonstration of Python OOP and DPG principles.
"""

# Immutable choices: optional tuple feature in the assignment.
CAMPUSES = ("Freetown Campus", "Hill Station Campus", "Online Learning")
LEVELS = ("Beginner", "Intermediate", "Advanced")


class Course:
    """A course that students can enroll in."""
    total_courses = 0

    def __init__(self, course_code, course_name, credits, level):
        if not self.is_valid_course_code(course_code):
            raise ValueError("Course code must have 3 letters followed by 3 digits.")
        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty.")
        if type(credits) is not int or credits <= 0:
            raise ValueError("Credits must be a positive whole number.")
        if level not in LEVELS:
            raise ValueError(f"Level must be one of: {LEVELS}")
        self.course_code = course_code
        self.course_name = course_name.strip()
        self.credits = credits
        self.level = level
        Course.total_courses += 1

    def display_info(self):
        return (f"[{self.course_code}] {self.course_name} - "
                f"{self.credits} Credits ({self.level})")

    @classmethod
    def get_total_courses(cls):
        return f"Total courses created: {cls.total_courses}"

    @staticmethod
    def is_valid_course_code(code):
        return (isinstance(code, str) and len(code) == 6
                and code[:3].isalpha() and code[:3].isascii()
                and code[3:].isascii() and code[3:].isdigit())


class Student:
    """A student; no phone number, home address or national ID collected."""
    total_students = 0

    def __init__(self, student_id, name, age, campus):
        if not self.is_valid_id(student_id):
            raise ValueError("Student ID must be STU followed by 3 digits.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")
        if not self.is_valid_age(age):
            raise ValueError("Student age must be a whole number from 15 to 70.")
        if campus not in CAMPUSES:
            raise ValueError(f"Campus must be one of: {CAMPUSES}")
        self.student_id = student_id
        self.name = name.strip()
        self.age = age
        self.campus = campus
        self.enrolled_course = None
        Student.total_students += 1

    def display_info(self):
        course = (self.enrolled_course.course_name
                  if self.enrolled_course else "Not enrolled")
        return (f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} "
                f"| Campus: {self.campus} | Course: {course}")

    def update_record(self, name=None, age=None):
        if name is not None:
            if not isinstance(name, str) or not name.strip():
                return "Update failed: name cannot be empty."
            self.name = name.strip()
        if age is not None:
            if not self.is_valid_age(age):
                return "Update failed: age must be between 15 and 70."
            self.age = age
        return "Record updated successfully."

    def enroll(self, course):
        if not isinstance(course, Course):
            return "Enrollment failed: invalid course."
        self.enrolled_course = course
        return f"{self.name} enrolled in {course.course_name}."

    @classmethod
    def get_total_students(cls):
        return f"Total student objects created: {cls.total_students}"

    @staticmethod
    def is_valid_id(student_id):
        return (isinstance(student_id, str) and len(student_id) == 6
                and student_id.startswith("STU")
                and student_id[3:].isascii() and student_id[3:].isdigit())

    @staticmethod
    def is_valid_age(age):
        return type(age) is int and 15 <= age <= 70


# One main collection: a list of Student objects (Task 2).
learning_portal = []


def add_student(student):
    if not isinstance(student, Student):
        return "Only Student objects can be added."
    for existing in learning_portal:
        if existing.student_id == student.student_id:
            return f"Student ID {student.student_id} already registered."
    learning_portal.append(student)
    return f"Added: {student.name}"


def display_all_students():
    if not learning_portal:
        print("No students in portal yet.")
        return
    print("--- All Students in Learning Portal ---")
    for student in learning_portal:
        print(student.display_info())
    print("---------------------------------------")


if __name__ == "__main__":
    # Ten example courses, each created as a Course object.
    course_details = [
        ("EDU101", "Introduction to Python", 3, LEVELS[0]),
        ("EDU102", "Digital Literacy", 2, LEVELS[0]),
        ("EDU103", "Computer Fundamentals", 3, LEVELS[0]),
        ("EDU104", "Web Development", 3, LEVELS[1]),
        ("EDU105", "Database Fundamentals", 3, LEVELS[1]),
        ("EDU106", "Object-Oriented Programming", 3, LEVELS[1]),
        ("EDU107", "Computer Networking", 3, LEVELS[1]),
        ("EDU108", "Cybersecurity Basics", 2, LEVELS[1]),
        ("EDU109", "Data Analysis", 3, LEVELS[2]),
        ("EDU110", "Software Engineering", 3, LEVELS[2]),
    ]
    courses = [Course(*details) for details in course_details]

    print("--- Available Courses ---")
    for course in courses:
        print(course.display_info())
    print(Course.get_total_courses())
    print(f"Is EDU101 valid? {Course.is_valid_course_code('EDU101')}")
    print()

    # Fictional sample students for demonstration (not real student records).
    student_details = [
        ("Mariama Kargbo", 20), ("Joseph Sesay", 22),
        ("Fatmata Kamara", 19), ("Ibrahim Koroma", 21),
        ("Aminata Bangura", 20), ("Mohamed Conteh", 23),
        ("Hawa Turay", 18), ("Abdul Jalloh", 22),
        ("Zainab Mansaray", 21), ("Samuel Fofanah", 24),
        ("Isatu Kallon", 20), ("Alhaji Bah", 19),
        ("Kadiatu Sankoh", 22), ("Sorie Kanu", 21),
        ("Adama Sheriff", 23), ("Brima Suma", 20),
        ("Fatu Cole", 19), ("Osman Rogers", 22),
        ("Memunatu Dumbuya", 21), ("Patrick Williams", 24),
        ("Yabom Sesay", 20), ("Abubakar Kamara", 23),
        ("Ramatu Koroma", 19), ("David Bangura", 22),
        ("Haja Conteh", 21), ("Sahr Jalloh", 20),
        ("Kadija Turay", 18), ("Alusine Mansaray", 24),
        ("Bintu Fofanah", 22), ("Emmanuel Kallon", 21),
    ]

    for index, (name, age) in enumerate(student_details):
        student_id = f"STU{index + 1:03d}"
        campus = CAMPUSES[index % len(CAMPUSES)]
        student = Student(student_id, name, age, campus)
        course = courses[index % len(courses)]
        print(student.enroll(course))
        print(add_student(student))

    # Demonstrate updating a record and preventing duplicate registration.
    print(learning_portal[0].update_record(age=21))
    print(add_student(learning_portal[0]))
    print()
    display_all_students()
    print(Student.get_total_students())
    print(f"Students registered in list: {len(learning_portal)}")
    print(f"Available campuses: {CAMPUSES}")
    print(f"Learning levels: {LEVELS}")
