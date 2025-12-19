# GSE301 Python Fundamentals Project
# Students Academic Performance Analysis System
# Name: Oyinlye Matthew
# Matric Number: 22/56EG089


# ======================================
# Part 1: DATA COLLECTION AND STORAGE
# ======================================



# Task 1.1: Variable Declaration and Data Types
student_name = "DevTimmy Oyin"
matric_number = "22/56EG089"
age = 22
cgpa = 4.52
is_active = True
course_registered = ["GSE301", "Data Science", "Analysis", "Statistics"]
grades = {
    "GSE301": "A",
    "Data Science": "B",
    "Analysis": "B",
    "Statistics": "A"
}



# Task 1.2: Structuring the Data collected

# Lists, disctionaries, sets, tuples
student_names = [
    "Rasheed Fatia",
    "DevTimmy Oyin",
    "Olaosebikan Michael",
    "Timi Abidoye",
    "Nimah Farouk"
]

# disctionary for each students full profile

students_data = {
    "Rasheed Fatia" : {
        "matric number": "22/45AB011",
        "age": 21,
        "cgpa": 4.07,
        "is_active" : True,
        "courses_registered" : ["GSE301", "BioChemistry", "Analysis", "Statistics"],
        "grades" : {
             "GSE301": "A",
             "Data Science": "A",
             "Analysis": "B",
             "Statistics": "C"
        },
         "outstanding_courses": 0
    },

     "DevTimmy Oyin" : {
        "matric number": "22/56EG089",
        "age": 22,
        "cgpa": 4.52,
        "is_active" : True,
        "courses_registered" : ["GSE301", "Data Science", "Analysis", "Statistics"],
        "grades" : {
            "GSE301": "A",
            "Data Science": "B",
            "Analysis": "B",
            "Statistics": "A"
        },
         "outstanding_courses": 0
    },

     "Olaosebikan Michael" : {
        "matric number": "22/45BY084",
        "age": 25,
        "cgpa": 2.56,
        "is_active" : False,
        "courses_registered" : ["GSE301", "BioChemistry", "Engineering", "Data Engineering"],
        "grades" : {
             "GSE301": "D",
             "BioChemistry": "C",
             "Engineering": "B",
             "Data Engineering": "D"
        },
         "outstanding_courses": 0
    },

     "Timi Abidoye" : {
        "matric number": "22/45AB011",
        "age": 21,
        "cgpa": 4.87,
        "is_active" : True,
        "courses_registered" : ["GSE301", "BioChemistry", "Statistics", "Artificial Intelligence"],
        "grades" : {
             "GSE301": "A",
             "BioChemistry": "C",
             "Statistics": "B",
             "Artificial Intelligence": "E"
        },
         "outstanding_courses": 0
    },

     "Nimah Farouk" : {
        "matric number": "22/45AB011",
        "age": 20,
        "cgpa": 2.97,
        "is_active" : True,
        "courses_registered" : ["GSE301", "Web Dev", "Networking", "Database Design"],
        "grades" : {
             "GSE301": "A",
             "Web Dev": "E",
             "Networking": "B",
             "Database Design": "C"
        },
        "outstanding_courses": 0
    }
}

# Set to store unique courses offered in the department

unique_courses = {
    "GSE301", "Web Dev", "Networking", "Database Design", "Statistics",
    "Artificial Intelligence", "BioChemistry", "Engineering", "Data Engineering",
    "Data Science", "Analysis"
}

# Tuple for fixed department information
department_info = ("Statistics", "Physical Sciences", 2025)


#Print confirmation
print(f"\n Loading Students records...")
print(f"{len(students_data)} student profiles loaded successfully.")
print(f"Department: {department_info[0]}")
print(f"Faculty: {department_info[1]}");
print(f"Year: {department_info[2]}")


# Task 2.1: Grading Function

def calculate_grade(score):
    """
    Convert numerical score (0-100) to a letter grade 
    and provide feedback
    """

    # Determin grade using IF/ELIF/ELSE

    if score >= 70: grade = "A"
    elif score >=60: grade = "B"
    elif score >= 50: grade = "C"
    elif score >= 45: grade = "D"
    elif score >= 40: grade = "E"
    else : grade = "F"

    #giving feedback using MATCH/CASE
    match grade: 
        case "A": feedback= "Excellent grade"
        case "B": feedback= "Ver Good Keep up the great work"
        case "C": feedback= "Good Job! You passed satisfactorily"
        case "D": feedback= "Fair Performance. Consider improvement"
        case "E": feedback= "Passed, but need significant improvement"
        case "F": feedback= "Failed, you'll have to retake this course"
        case _: feedback= "Invalid grade"

    return grade, feedback


# Task 2.2: Input Validation Function
def validate_student_input():
    """
    Get User input for age and CGPA with validation
    Uses type conversion and TRY/Except for error handling
    """

    print("\n--- Input Validation Demo ---")

    #validate Age
    while True:
        try:
            age_input = input("Enter student's age (16-40): ")
            age = int(age_input) # Converted string to int

            # validate range

            if 16 <= age <= 40:
                print(f" Age Matched Successfully: {age}")
                break
            else:
                print(" Age must be between 16 and 40. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number for age")

        # Validate cgpa
        while True:
            try:
                cgpa_input = input("Enter student's CGPA (0.0 - 5.0): ")
                cgpa = float(cgpa_input) #Converted string to float

                # Validate Range
                if 0.0 <= cgpa <= 5.0:
                    print(f"CGPA matched successfully: {cgpa}")
                    break
                else:
                    print("Invalid CGPA, Try again")
            except ValueError:
                print("Invalid Input! Enter a valid number for CGPA")
        return age, cgpa


# Function for grading system
def demonstrate_grading():
    """
    Show the grading system in action
    """

    print("\n--- Grading System Demonstration ---")
    test_scores = [85, 65, 43, 38, 25]

    for score in test_scores:
        grade, feedback = calculate_grade(score)
        print(f"Score: {score} Grade: {grade} {feedback}")


# ==============================================
# Part 3: ANALYSIS AND REPORTING
# ==============================================

# Task 3.1: List Operations
def demonstrate_list_slicing():
    """
    Shows various list slicing operation on assignment score
    """

    print("\n--- List Slicing Demonstration ---")

    # List of 100 assignment cores
    assignment_scores = [78, 85, 92, 67, 88, 95, 73, 81, 90, 86]

    print(f"All Assignment scores: {assignment_scores}")

    # Extract the top 3 scores using slicing
    top_3_scores = assignment_scores[:3]
    print(f"\n Top 3 Scores: {top_3_scores}")


    # Extract the last 5 scores using negative indexing
    last_5_scores = assignment_scores[-5:]
    print(f"\n last 5 scores: {last_5_scores}")

    # Extract every other scores using step slicing
    other_scores = assignment_scores[::2]
    print(f"\n Other Score: {other_scores}")

    # Extract scores in reverse //Bonus section
    reversed_scores = assignment_scores[::-1]
    print(f"Scores in reverse: {reversed_scores}")

    return assignment_scores


# Task 3.2: Set Operations
def perform_set_operations():
    """
    Demonstrates set operations on student data
    """
    print("\n--- Set Operations Demonstration ---")

    # Set of students who passed Python
    set_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Timi Abidoye", "Moses Oyedele"}

    # Set of students with CGPA above 4.0
    set_merit = {"Rasheed Fatia", "Timi Abidoye", "Nimah Nina"}

    print(f"Students who passed Python: {set_pass}")
    print(f"Students with CGPA above 4.0: {set_merit}")


    # Intersection: Students who passed AND have merit
    pass_and_merit = set_pass.intersection(set_merit)

    print(f"\n Students who passed Python AND have merit (intersection): ")
    print(f"{pass_and_merit}")
    

    #Union: All distinct students in both sets
    all_students = set_pass.union(set_merit)

    print(f"\n All distinct students in both sets (union): ")
    print(f"{all_students}")

    # Difference: Students who passed but do NOT have merit
    pass_no_merit = set_pass.difference(set_merit)
    print(f"\nStudents who passed Python but do NOT have merit (difference):")
    print(f"{pass_no_merit}")

    # Bonus: Symmetric Difference (Students in either set but not both)
    either_not_both = set_pass.symmetric_difference(set_merit)

    print(f"\nStudents in either set but NOT both (symmetric difference):")
    print(f"{either_not_both}")
    
    return set_pass, set_merit


 # Analysis function to find students with high performance
def analyze_student_performance():
    """
    Analyze and display student performance statistics
    """

    print("\n--- Student Performance Analysis ---")

    #calculte average CGPA
    total_cgpa = sum(student["cgpa"] for student in students_data.values())
    average_cgpa = total_cgpa / len(students_data)

    print(f"Total students: {len(students_data)}")
    print(f"Average CGPA: {average_cgpa:.2f}")


    # Find students with CGPA above 4.0
    high_performers = [name for name, data in students_data.items() if data["cgpa"] >= 4.0]
    print(f"\n High performers (CGPA >= 4.0: {len(high_performers)}")
    for name in high_performers:
        print(f" - {name}: {students_data[name]['cgpa']}")


    # Find students with outstanding courses
    students_with_outstanding = [name for name, data in students_data.items() if data["outstanding_courses"] > 0]

    print(f"\nStudents with outstanding courses: {len(students_with_outstanding)}")
    for name in students_with_outstanding:
        print(f"  - {name}: {students_data[name]['outstanding_courses']} course(s)")

# ========================================
# PART 4: INTERACTIVE MENU SYSTEM
# ========================================

def display_menu():
    """
    Displays the main menu options

    """

    print("\n" + "="*50)
    print("   Student Academic Performance System")
    print("="*50)
    print("Menu Options")
    print("1. View All students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Process nested student scores (Advanced)")
    print("6. Type detection demo (Advanced)")
    print("7. Interactive type checker (Advanced)")
    print("8. Exit")
    print("-"*50)

def view_all_students():
    """
    Display all students in the system
    """

    print("\n--- List of Students ---")
    for index, name in enumerate(student_names, start=1):
        print(f"{index}. {name}")
    print("-"*50)


def add_new_student():
    """
    Adds a new student to the system
    """

    print("\n--- Add new Student ---")

    try: 
        # Get student information
        name = input("Enter Name: ").strip()
        matric = input("Enter matric number: ").strip()

        age_input = input("Enter age: ").strip()
        age = int(age_input)

        cgpa_input = input("Enter CGPA: ").strip()
        cgpa = float(cgpa_input)

        # Validate age and CGPA
        if not (16 <= age <= 40):
            print("Age must be between 16 and 40.")
            return
        
        if not (0.0 <= cgpa <= 5.0 ):
            print("CGPA must be between 0.0 and 5.0")
            return
        
        active_input = input("Is the student active (yes/no): ").strip().lower()
        is_active = active_input == "yes" or active_input == "y"

        courses_input = input("Enter courses (comma separated): ").strip()
        courses = [course.strip() for course in courses_input.split(",")]

        # Create student record
        students_data[name] = {
            "matric_number": matric,
            "age": age,
            "cgpa": cgpa,
            "is_active": is_active,
            "courses_registered": courses,
            "grades": {},
            "outstanding_courses": 0
        }


        # Add to student names list
        student_names.append(name)

        print(f"student record added successfully.")
        print("-"*50)

    except ValueError:
        print(" Invalid input! Please enter correct data types.")
        print("-"*50)

def check_graduation_eligibility(student_name):
    """
    Check if a students is eligible for graduation
    Uses logival operators (and, or) to determine eligibility
    """
    print("\n Checking eligibility...")

    # Check if student exists

    if student_name not in students_data:
        print(f" Student '{student_name}' not found in records.")
        return False, "Student not found."

     # Get student data
    student = students_data[student_name]

    # Display student information
    print(f"Matric Number: {student['matric_number']}")
    print(f"CGPA: {student['cgpa']}")
    print(f"Outstanding Courses: {student['outstanding_courses']}")
    print(f"Active Status: {student['is_active']}")

    print("\n Elibility Result:")


    cgpa_requirement = student['cgpa'] >= 2.5
    no_outstanding = student['outstanding_courses'] == 0
    active_status = student['is_active']


    # Check elibility using AND Operator
    is_eligible = cgpa_requirement and no_outstanding and active_status

    # Generate detailed message
    if is_eligible:
        message = f"{student_name} is eligible for graduation"
        print(f" {message}")
    else:
        message = f"{student_name} is NOT eligible for graduation."
        print(f" {message}")

        # show reasons for ineligibility
        print("\n Reasons: ")
        if not cgpa_requirement:
            print(f" - CGPA ({student['cgpa']}) is below 2.5")
        if not no_outstanding:
            print(f" - Has {student['outstanding_courses']} outstanding courses(s)")
        if not active_status:
            print(f" - Student is not active")

    print("-"*50)
    return is_eligible, message

def find_top_performer():
    """
    Find and displays the student with highest CGPA
    """

    print("\n--- Top Performer ---")

    if not students_data:
        print("No Student records available.")
        return

    # Find student with highest CGPA
    top_student = max(students_data.items(), key=lambda x: x[1]['cgpa'])
    name, data = top_student

    print(f"Name: {name}")
    print(f"Matric: {data['matric_number']}")
    print(f"CGPA: {data['cgpa']}")
    print(f"Courses: {data['courses_registered']}")
    print("-"*50)

def run_menu():
    """
    Run the interactive menu system
    """  
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Use MATCH/CASE for many navigation
        match choice:
            case "1":
                view_all_students()
            
            case "2":
                add_new_student()

            case "3":
                student_name = input("Enter student name: ").strip()
                check_graduation_eligibility(student_name)

            case "4":
                find_top_performer()
            
            case "5":
                process_nested_student_scores()

            case "6":
                demonstrate_type_detection()
            
            case "7":
                interactive_type_checker()

            case "8":
                print("\n Exiting the system...")
                print("Goodbye!")
                break

            case _:
                print("\n Invalid choice, please enter a number between 1 and 5.")


# =======================================
# PART 5: ADVANCED CHALLENGES (Optional)
# =======================================


# Task 5.1: Nested Data Processing

def process_nested_student_scores():
    """
    Process nested dictionary of students and their scores
    Calculate average scores and identify high performers
    """

    print("\n--- Nested Data Processing ---")


    # Nested dictionary: students with their course scores
    student_scores = {
        "Rasheed Fatia": {
            "GSE301": 85,
            "Data Science": 90,
            "Statistics": 78
        },
        "DevTimmy Oyin": {
            "GSE301": 92,
            "Data Science": 88,
            "Analysis": 95,
            "Statistics": 91
        },
        "Timi Abidoye": {
            "GSE301": 96,
            "BioChemistry": 72,
            "Statistics": 89,
            "AI": 94
        },
        "Olaosebikan Michael": {
            "GSE301": 55,
            "BioChemistry": 68,
            "Engineering": 71,
            "Data Engineering": 58
        },
        "Nimah Farouk": {
            "GSE301": 82,
            "Web Dev": 65,
            "Networking": 75,
            "Database Design": 69
        }
    }

    print("Student Scores Summary: ")
    print("-" * 60)

    # Calculate average score for each student
    for student_name, courses in student_scores.items():
        # Calculate average
        total_score = sum(courses.values())
        num_courses = len(courses)
        average = total_score / num_courses


        print(f"\n{student_name}:")
        print(f" Courses taken: {num_courses}")
        print(f" Total score: {total_score}")
        print(f" Average score: {average:.2f}")


        # Show individual course scores
        print(f" Course breakdown:")
        for course, score in courses.items():
            print(f" -{course}: {score}")

    print("\n" + "=" * 60)
    print("High Performers (Above 70 in ALL courses):")
    print("="*60)

    # Identify students who scored above in ALL registered courses
    high_performers = []

    for student_name, courses in student_scores.items():
        # Check if ALL scores are above 70
        all_above_70 = all(score > 70 for score in courses.values())

        if all_above_70:
            high_performers.append(student_name)
            avg_score = sum(courses.values()) / len(courses)
            print(f"\n {student_name}")
            print(f" Average: {avg_score:.2f}")
            print(f" All {len(courses)} courses scored above 70!")
    
    if not high_performers:
        print("\n No students scored above 70 in ALL courses.")

    print("-"*60)
    return student_scores


# Task 5.2: Pattern Matching with Type Detection
def detect_data_type(data):
    """
    Uses MATCH/CASE to identify the type of input
    and return a formatted summary
    """

    # Use match/case with type() to detect data type
    match type(data).__name__:
        case "int":
            return f"Type: Integer\nValue: {data}\nIs Even: {data % 2 == 0}\nAbsolute Value: {abs(data)}"
        
        case "float":
            return f"Type: Float\nValue: {data}\nRounded: {round(data, 2)}\nIs Positive: {data > 0}"
        
        case "str":
            return f"Type: String\nValue: '{data}'\nLength: {len(data)}\nUppercase: {data.upper()}\nLowercase: {data.lower()}"
        case "list":
            return f"Type: List\nLength: {len(data)}\nFirst element: {data[0] if data else 'N/A'}\nLast element: {data[-1] if data else 'N/A'}\nContents: {data}"
        
        case "dict":
            return f"Type: Dictionary\nNumber of keys: {len(data)}\nKeys: {list(data.keys())}\nValues: {list(data.values())}"
        
        case "tuple":
            return f"Type: Tuple\nLength: {len(data)}\nIs Immutable: Yes\nContents: {data}"
        
        case "set":
            return f"Type: Set\nSize: {len(data)}\nIs Unique: Yes\nContents: {data}"
        
        case "bool":
            return f"Type: Boolean\nValue: {data}\nNegation: {not data}"
        
        case _:
            return f"Type: Unknown ({type(data).__name__})\nValue: {data}"
        
    
def demonstrate_type_detection():
    """
    Demonstrate the type detection function with various data types
    """

    print("\n--- Type Detection with MATCH/CASE ---")
    print("="*60)

    # Test different data types
    test_data = [
        42,                                         # int
        3.14159,                                    # float
        "Hello, GSE301!",                           # str
        [10, 20, 30, 40, 50],                       # list
        {"name": "John", "age": 25, "cgpa": 4.5},   # dict
        ("Python", "Java", "C++"),                  # tuple
        {1, 2, 3, 4, 5},                            # set
        True                                        # bool
    ]

    for index, data in enumerate(test_data, start=1):
        print(f"\nTest {index}:")
        print("-" * 60)
        result = detect_data_type(data)
        print(result)

    print("\n" + "=" * 60)

# Interactive type checker
def interactive_type_checker():
    """
    Allow user to input data and check it's type
    """

    print("\n --- Interactive Type Checker ---")
    print("Enter a value to chec it's type (or 'quit' to exit)")

    while True:
        user_input = input("\nEnter value: ").strip()

        if user_input.lower() == 'quit':
            break

        # Try to convert to appropriate type
        try:
            # Try int
            if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
                data = int(user_input)

            # Try float
            elif '.' in user_input:
                data = float(user_input)
            
            # Otherwise keep as string
            else:
                data = user_input

            print("\n" + "-" * 60)
            result = detect_data_type(data)
            print(result)
            print("-"*60)
        
        except ValueError:
            print("Could not process the input. Treating as string.")
            result = detect_data_type(user_input)
            print(result)



# ====================================
# MAIN PROGRAM
# ====================================

def main():
    """
    Main function that runs the entire program
    """

    print("\n Loading student record...")
    # Menu loop goes in here
    print("Goodbye!")

    print(f"{len(students_data)} student profiles loaded successfully")
    print(f"Department: {department_info[0]}")


    # Test part 2: grading and validation
    demonstrate_grading()
    demonstrate_list_slicing()
    # validate_student_input()
    perform_set_operations()
    analyze_student_performance()

    # Run the interactive menu
    run_menu()



#Run the program
if __name__ == "__main__":
    main()
  