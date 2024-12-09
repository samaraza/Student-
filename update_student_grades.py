
def update_student_grades(students_grade,clear_terminal):

  try:
    clear_terminal()
    if not students_grade:
        print("No students available ")
        input("\nPress Enter to return to the main menu...")
        return
    name = input("Enter the name of the student to update: ")
    if name not in students_grade:
        print("Student not found")
    else:
        subject1 = input("Enter new grade for subject1: ")
        subject2 = input("Enter new grade for subject2: ")
        subject3 = input("Enter new grade for subject3: ")
        students_grade[name]= {"grade1": subject1, "grade2": subject2, "grade3": subject3}
        print(f"Grades  for {name} have been updated successfully. ")
  except ValueError:
    print("Invalid input. Please enter numeric values for grades.")
  except Exception as e:
      print(f"An error occurred: {e}")
  input("\nPress Enter to return to the main menu... ")


