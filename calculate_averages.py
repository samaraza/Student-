
def calculate_averages(students_grade, clear_terminal):
  try:
    clear_terminal()
    print("Student Averages:  ")
    for name , grade in students_grade.items():
        average = (float(grade['grade1']) + float(grade['grade2']) + float(grade['grade3']))
        print(f"{name}: {average} ")
  except KeyError:
      print("Missing grade information for a student.")
  except Exception as e:
      print(f"An error occurred: {e}")
  input("\nPress Enter to return to the main menu... ")
