
def list_students(students_grade, clear_terminal):
    while True:
      try:
        clear_terminal()
        print("students_grade: ")
        for name in students_grade:
            student_info = students_grade[name]
            print(f"name: {name}, subject1: {student_info['grade1']}, subject2: {student_info['grade2']}, subject3: {student_info['grade3']} ")
      except KeyError:
          print("Some students have incomplete grade information.")
      except Exception as e:
          print(f"An error occurred: {e}")
      choices = input("Do you want to add another student? (y/n): ")
      if choices.lower() != "y":
            break


