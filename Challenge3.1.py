subjects = ["physics", "calculus", "poetry", "history"]
grades = ["98", "97", "85", "88"]
subjects.append("computer_science")
grades.append("100")
grade_book = list(zip(subjects, grades))
grade_book.append(("visual arts", "93"))
print(grade_book)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
full_gradebook= last_semester_gradebook + grade_book
print(full_gradebook)






# last_semester_gradebook = [("physics", 80), ("calculus", 96), ("poetry", 97), ("history", 65)]
#     grade_book = list(zip()