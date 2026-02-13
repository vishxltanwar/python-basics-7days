#Check if a number is positive, negative, or zero.
"""
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
"""

#Print numbers from 1 to 10 using a loop.
"""
for i in range(1, 11):
    print(i)
"""

#Password checker
"""
password = "secret123"
Enter_password = input("Enter the password: ")
if Enter_password == password:
    print("Access granted.")
else:
    print("Access denied.")
"""

#Give 3 attempts using a loop
#Lock access after 3 wrong tries
password = "secret123"
attempts = 3
while attempts > 0:
    Enter_password = input("Enter the password: ")
    if Enter_password == password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print(f"Access denied. You have {attempts} left.")
        if attempts == 0:
            print(f"Access Locked. Please try again later.")