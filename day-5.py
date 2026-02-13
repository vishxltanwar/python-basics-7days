#Take a name as input and:
#Print it in uppercase
#Print first and last character
#Print reversed string
"""
name = input("Enter your name: ")
print("Uppercase: ", name.upper())
print("First character: ",name[0])
print("Last character: ",name[-1])
print("Reversed name:",name[::-1])
print(f"My name is {name}, and it has {len(name)} characters")
"""

#Count vowels in a word.
"""
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"The word '{word}' has {count} vowels.")
"""

#Check if a string is a palindrome.
"""
word = input("Enter a word: ")
if word ==word[::-1]:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")
"""

#Mini project
#Create a Password Strength Checker
#Rules:
#Length ≥ 8
#Must contain:
#1 uppercase
#1 lowercase
#1 digit

password = input("Enter a password: ")

length_check = len(password) >= 8
upper_check = any(char.isupper() for char in password)
lower_check = any(char.islower() for char in password)
digit_check = any (char.isdigit() for char in password)

if length_check and upper_check and lower_check and digit_check:
    print("Password is strong.")
else:
    print("Password is weak. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")

