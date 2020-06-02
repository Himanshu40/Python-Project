# Project : Gradebook
# Date    : Tue 02 Jun 2020 09:14:38 AM IST

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = zip(subjects, grades)

print(list(gradebook))

subjects.append("computer science")
grades.append(100)
gradebook = zip(subjects, grades)
gradebook.append(("visual arts", 93))

full_gradebook = zip(last_semester_gradebook, gradebook)

print(list(gradebook))
print(list(full_gradebook))