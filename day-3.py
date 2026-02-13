#Create a function to check even or odd
"""
def num(number):
    if number % 2 == 0:
        return "Even"
    elif number % 2 != 0:
        return "Odd"
number = int(input("Enter a number: "))
print(num(number))
"""

#Function to calculate simple interest
"""
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print("The simple interest is:", simple_interest(principal,rate,time))
"""

#Function that takes name & prints

def intro(name,city):
    return f"My name is {name}, city is {city}"
name = input("Enter your name: ")
city = input("Enter your city: ")
print(intro(name,city))