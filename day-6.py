#Create a program that:
#Asks user for their name
#Saves it to a file users.txt
#Handles error if file can't open
#Displays all saved names
"""
try:
    name = input("Enter your name: ")

    with open("users.txt", "a") as file:
        file.write(name + "\n")

    print("Saved successfully!")

    print("\nAll Users:")
    with open("users.txt", "r") as file:
        for line in file:
            print(line.strip())

except Exception as e:
    print("Something went wrong:", e)
"""

#remove a name from the file
with open("users.txt", "r") as file:
    names = file.readlines()

name_to_remove = input("Enter the name to remove: ")

if name_to_remove.strip() in [name.strip() for name in names]:
    names = [name for name in names if name.strip() != name_to_remove.strip()]

    with open("users.txt", "w") as file:
        file.writelines(names)

    print("Name removed successfully!")
else:
    print("Name not found!")    

with open("users.txt", "r") as file:
    print("\nAll Users:")
    for line in file:
        print(line.strip())