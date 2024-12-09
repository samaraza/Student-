import os
from add_student import add_student
from calculate_averages import calculate_averages
from list_students import list_students
from top_performer import top_performer
from update_student_grades import update_student_grades

students_grade = {}

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
while True:
  try:
    print("1. Add Student: ")
    print("2. View Students and Grades: ")
    print("3. Calculate Averages: ")
    print("4. Find Top Performer: ")
    print("5. Update Student Grades: ")
    print("6. Exit: ")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_student(students_grade, clear_terminal)
    elif choice == "2":
        list_students(students_grade, clear_terminal)
    elif choice == "3":
        calculate_averages(students_grade, clear_terminal)
    elif choice == "4":
        top_performer(students_grade, clear_terminal)
    elif choice == "5":
        update_student_grades(students_grade, clear_terminal)
    elif choice == "6":
        print("Exiting the program ")
        break
    else:
        print("Invali choice, Please enter a number between 1 and 6 ")
  except Exception as e:
      print(f"An  error occurred: {e}")
      input("\nPress Enter to return to the main menu...")

