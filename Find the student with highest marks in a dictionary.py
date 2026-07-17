marks = {
    "Aman": 85,
    "Riya": 92,
    "Neha": 78,
    "Karan": 95
}

highest = max(marks, key=marks.get)

print("Student with highest marks:", highest)
print("Marks:", marks[highest])
