#Create a list of 5 numbers and:
#print sum
#print max & min
"""
numbers = [10, 20, 30, 40, 50]
print("Sum of numbers:", sum(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
"""

#Create a tuple of your favorite subjects and print each using a loop.
"""
favourite_subjects = ("Maths", "Science", "History", "Literature", "Art")
for subjects in favourite_subjects:
    print(subjects)
"""

#Take a list with duplicate values and convert it to a set.
"""
values = [1, 2, 3, 4, 5, 2, 3, 1]
unique_values = set(values)
print("Unique values:", unique_values)
"""

#Create a dictionary with:
#name
#age
#skills (as a list)
intro_dict = {
    "name": "Vishal", 
    "age": 25, 
    "skills": ["Python", "JavaScript", "SQL"]
    }
for key, values in intro_dict.items():
    print(f"{key}: {values}")