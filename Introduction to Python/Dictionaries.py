students = {"Bob":13,"Mariana":14,"Gabriela":15,"Beatriz":16}
print(students)

print(students["Mariana"])

print(students.keys())
print(students.values())

students["Beatriz"] = 17
print(students)

del students["Bob"]
print(students)

print(len(students))