Hello = "Hello World"

print(Hello)

users_name = input("What is your name? ")
print("Hello " + users_name)

birth_year = input("What is your birth year? ")
age = 2021 - int(birth_year)
print("Your age is " + str(age))

number1 = input("Enter a number ")
number2 = input("Enter a second number ")
sum = float(number1) + float(number2)
print("The sum of your two numbers is " + str(sum))

learning = "Learning Python"

# this returns the string uppercased
print(learning.upper())

# this returns the string lowercased
print(learning.lower())

# this returns the index of y
print(learning.find("y"))

# this returns the index of the word Python in the string
print(learning.find("Python"))

# this returns a -1 because the letter x is NOT in the string
print(learning.find("x"))

# this replaced the word Learning for Learned in the string
print(learning.replace("Learning", "Learned"))

