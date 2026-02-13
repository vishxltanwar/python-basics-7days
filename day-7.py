#Student Record System
students = []

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    students.append({"name": name, "marks": marks})

print("\nStudent Records:")
for student in students:
    print(f"{student['name']} scored {student['marks']}")
