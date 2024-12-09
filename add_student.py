
def add_student(students_grade, clear_terminal):
    while True:
      try:
        clear_terminal()
        name = input("Enter student's name: ")
        subject1 = input("Enter grade for subject1: ")
        subject2 = input("Enter grade for subject2: ")
        subject3 = input("Enter grade for subject3: ")

        students_grade[name]= {"grade1": subject1, "grade2": subject2, "grade3": subject3}
        print(f"Student {subject1}, {subject2}, {subject3} added to the catalog with name {name} ")
      except ValueError:
          print("Invalid input. please enter numeric values for grades. ")
      except Exception as e:
          print(f"An unexpected error occurred: {e}")

      choice = input("Do you want to add another student? (y/n): ")
      if choice.lower() != "y":
            break
