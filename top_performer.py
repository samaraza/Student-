
def top_performer(students_grade, clear_terminal):
  try:
    clear_terminal()
    if not students_grade:
        print("No students available ")
        input("\nPress Enter to return to the main menu...")
        return
    top_student = None
    top_average = 0

    for name, grade in students_grade.items():
        average = (float(grade['grade1']) + float(grade['grade2']) + float(grade['grade3']))
        if average > top_average:
            top_average = average
            top_student = name
    print(f"Top Performer: {top_student} with  an average of {top_average}")
  except KeyError:
    print("Missing grade information for a student.")
  except Exception as e:
      print(f"An error occurred: {e}")
  input("\nPress Enter to return to the main menu... ")