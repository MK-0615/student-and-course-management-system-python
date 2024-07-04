# Global Lists for Course and Student Data
coursecodelst = ["FHCT1024", "FHCT1014", "FHMM1034"]
coursedesclst = ["PROGRAMMING CONCEPTS AND DESIGN", "INTRODUCTION TO DATA ANALYTICS", "MATHEMATICS III"]
coursetestlst = [["T1", "T2", "A", "F"], ["T1", "T2", "A", "F"], ["T1", "T2", "A", "F"]]
coursemarklst = [[50, 50, 100, 100], [50, 50, 100, 100], [50, 50, 100, 100]]
courseperclst = [[0.10, 0.20, 0.20, 0.50], [0.10, 0.20, 0.20, 0.50], [0.10, 0.20, 0.20, 0.50]]
studentidcourse = [["2200012", "2200011", "2210001", "2113001", "2217033", "2200013", "2200014", "2200015", "2200016", "2200017"],
                   ["2200071", "2200072", "2200073", "2200074", "2200075", "2200076", "2200077", "2200078", "2200079", "2200080"],
                   ["2220001", "2220002", "2220003", "2220004", "2220005", "2220006", "2220007", "2220008", "2220009", "2220010"]]
studentnamecourse = [["John Anthony", "Jamie Crossby", "Tan Yin Jing", "Chia Xi Xin", "Ahmand Ali", "Natasha", "Daniel", "Adrian Wong", "Soo Ai Ling", "Adam Lee"],
                     ["Jake Chan", "Tony Phoon", "Frederick Wong", "Sammuel Sam", "Patrick Ray", "Lay Nona", "Cobby Fay", "Charlie Marry", "Marry Terry", "Pocky Locky"],
                     ["Vary Potter", "Patty Bane", "Vane Canny", "Tabby Bonny", "Lacy Winny", "Rosy Fanny", "Gobby Horlie", "Kinny Lorry", "Porry Ferry", "Gotty Dawn"]]

marklist = [[0] * len(coursetestlst[i]) for i in range(len(coursecodelst))]
gradelist = [[0] * len(coursetestlst[i]) for i in range(len(coursecodelst))]

# Function to Print System Configuration Header
def systemcfg():
    print("-" * 80)
    print("Main - Course Learning Outcomes Assessment System")
    print("-" * 80)

# Function to Print Courses and Description
def courses():
    print("Courses:")
    for i in range(len(coursecodelst)):
        print(f"{i + 1}. {coursecodelst[i]} - {coursedesclst[i]}")
    print("-" * 80)

# Function to Add Course
def add_course():
    new_code = input("Enter new course code: ")
    new_desc = input("Enter course description: ")
    coursecodelst.append(new_code)
    coursedesclst.append(new_desc)
    coursetestlst.append([])
    coursemarklst.append([])
    courseperclst.append([])
    studentidcourse.append([])
    studentnamecourse.append([])
    marklist.append([])
    gradelist.append([])
    print(f"Course {new_code} - {new_desc} added successfully.")

# Function to Update Course
def update_course():
    courses()
    choice = int(input("Enter the number of the course to update: ")) - 1
    new_code = input(f"Enter new course code (currently {coursecodelst[choice]}): ")
    new_desc = input(f"Enter new course description (currently {coursedesclst[choice]}): ")
    coursecodelst[choice] = new_code
    coursedesclst[choice] = new_desc
    print(f"Course {new_code} - {new_desc} updated successfully.")

# Function to Delete Course
def delete_course():
    courses()
    choice = int(input("Enter the number of the course to delete: ")) - 1
    del coursecodelst[choice]
    del coursedesclst[choice]
    del coursetestlst[choice]
    del coursemarklst[choice]
    del courseperclst[choice]
    del studentidcourse[choice]
    del studentnamecourse[choice]
    del marklist[choice]
    del gradelist[choice]
    print("Course deleted successfully.")

# Function to Print Assessment Types for Courses
def assessment_types():
    print("Assessment Types:")
    for i in range(len(coursecodelst)):
        print(f"{i + 1}. {coursecodelst[i]} - {coursedesclst[i]}")
        print("Assessment\tMark\tTotal Mark to Final")
        for j in range(len(coursetestlst[i])):
            print(f"{coursetestlst[i][j]}\t\t{coursemarklst[i][j]}\t\t{courseperclst[i][j]}")
        print("-" * 80)

# Function to Add Assessment Type
def add_assessment_type():
    courses()
    choice = int(input("Enter the number of the course to add assessment type: ")) - 1
    new_test = input("Enter new assessment type: ")
    new_mark = int(input("Enter total marks for this assessment type: "))
    new_perc = float(input("Enter percentage of total mark to final grade: "))
    coursetestlst[choice].append(new_test)
    coursemarklst[choice].append(new_mark)
    courseperclst[choice].append(new_perc)
    marklist[choice].append(0)
    gradelist[choice].append(0)
    print(f"Assessment type {new_test} added to course {coursecodelst[choice]}.")

# Function to Update Assessment Type
def update_assessment_type():
    assessment_types()
    choice = int(input("Enter the number of the assessment type to update: ")) - 1
    new_test = input(f"Enter new assessment type (currently {coursetestlst[choice]}): ")
    new_mark = int(input(f"Enter new total marks for this assessment type (currently {coursemarklst[choice]}): "))
    new_perc = float(input(f"Enter new percentage of total mark to final grade (currently {courseperclst[choice]}): "))
    coursetestlst[choice][choice] = new_test
    coursemarklst[choice][choice] = new_mark
    courseperclst[choice][choice] = new_perc
    print(f"Assessment type {new_test} updated successfully.")

# Function to Delete Assessment Type
def delete_assessment_type():
    assessment_types()
    choice = int(input("Enter the number of the assessment type to delete: ")) - 1
    del coursetestlst[choice]
    del coursemarklst[choice]
    del courseperclst[choice]
    del marklist[choice]
    del gradelist[choice]
    print("Assessment type deleted successfully.")

# Function to Print Students Enrolled in Courses
def student():
    print("Courses Student Maintenance:")
    for i in range(len(coursecodelst)):
        print(f"{i + 1}. {coursecodelst[i]} - {coursedesclst[i]}")
        if len(studentidcourse[i]) == 0:
            print("No students enrolled.")
        else:
            for j in range(len(studentidcourse[i])):
                print(f"{studentidcourse[i][j]} - {studentnamecourse[i][j]}")
        print("-" * 80)

# Function to Add Student
def add_student():
    courses()
    choice = int(input("Enter the number of the course to add student: ")) - 1
    new_id = input("Enter new student ID: ")
    new_name = input("Enter new student name: ")
    studentidcourse[choice].append(new_id)
    studentnamecourse[choice].append(new_name)
    marklist[choice].append(0)
    gradelist[choice].append(0)
    print(f"Student {new_name} added to course {coursecodelst[choice]}.")

# Function to Update Student
def update_student():
    student()
    choice = int(input("Enter the number of the student to update: ")) - 1
    new_id = input(f"Enter new student ID (currently {studentidcourse[choice]}): ")
    new_name = input(f"Enter new student name (currently {studentnamecourse[choice]}): ")
    studentidcourse[choice][choice] = new_id
    studentnamecourse[choice][choice] = new_name
    print(f"Student {new_name} updated successfully.")

# Function to Delete Student
def delete_student():
    student()
    choice = int(input("Enter the number of the student to delete: ")) - 1
    del studentidcourse[choice]
    del studentnamecourse[choice]
    del marklist[choice]
    del gradelist[choice]
    print("Student deleted successfully.")

# Function to Print Grades
def grades():
    print("Grades:")
    for i in range(len(coursecodelst)):
        print(f"{coursecodelst[i]} - {coursedesclst[i]}")
        print("Assessment\tStudent\tGrade")
        for j in range(len(coursetestlst[i])):
            for k in range(len(studentidcourse[i])):
                grade = int(marklist[i][j] * courseperclst[i][j])
                print(f"{coursetestlst[i][j]}\t\t{studentnamecourse[i][k]}\t{grade}")
        print("-" * 80)

# Function to Save Data to Text Files
def save_data():
    with open("courses.txt", "w") as f:
        for code, desc in zip(coursecodelst, coursedesclst):
            f.write(f"{code},{desc}\n")
    
    with open("assessment_types.txt", "w") as f:
        for i in range(len(coursecodelst)):
            for j in range(len(coursetestlst[i])):
                f.write(f"{coursecodelst[i]},{coursetestlst[i][j]},{coursemarklst[i][j]},{courseperclst[i][j]}\n")
    
    with open("students.txt", "w") as f:
        for i in range(len(coursecodelst)):
            for j in range(len(studentidcourse[i])):
                f.write(f"{coursecodelst[i]},{studentidcourse[i][j]},{studentnamecourse[i][j]}\n")
    
    with open("grades.txt", "w") as f:
        for i in range(len(coursecodelst)):
            for j in range(len(coursetestlst[i])):
                for k in range(len(studentidcourse[i])):
                    grade = int(marklist[i][j] * courseperclst[i][j])
                    f.write(f"{coursecodelst[i]},{coursetestlst[i][j]},{studentidcourse[i][k]},{grade}\n")

# Main Function to Handle User Interface
def main():
    while True:
        systemcfg()
        print("<C>ourses | <A>ssessment Types | <S>tudents  | <G>rades | <E>xit | <SA>ve")
        select = input("Select >> ").upper()
        
        if select == 'C':
            print("1. View Courses")
            print("2. Add Course")
            print("3. Update Course")
            print("4. Delete Course")
            option = int(input("Enter your choice: "))
            if option == 1:
                courses()
            elif option == 2:
                add_course()
            elif option == 3:
                update_course()
            elif option == 4:
                delete_course()
            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")
        
        elif select == 'A':
            print("1. View Assessment Types")
            print("2. Add Assessment Type")
            print("3. Update Assessment Type")
            print("4. Delete Assessment Type")
            option = int(input("Enter your choice: "))
            if option == 1:
                assessment_types()
            elif option == 2:
                add_assessment_type()
            elif option == 3:
                update_assessment_type()
            elif option == 4:
                delete_assessment_type()
            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")
        
        elif select == 'S':
            print("1. View Students")
            print("2. Add Student")
            print("3. Update Student")
            print("4. Delete Student")
            option = int(input("Enter your choice: "))
            if option == 1:
                student()
            elif option == 2:
                add_student()
            elif option == 3:
                update_student()
            elif option == 4:
                delete_student()
            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")
        
        elif select == 'G':
            grades()
        
        elif select == 'SA':
            save_data()
            print("Data saved successfully.")
        
        elif select == 'E':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid input. Please enter C, A, S, G, SA, or E.")

if __name__ == "__main__":
    main()
