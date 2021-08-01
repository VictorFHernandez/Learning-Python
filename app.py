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

# this returns a boolean depending if the word or letter is in the string
print("Python" in learning)

# different math operators, the '//' returns an rounded up numbers of the division and the  '**' is to the power of
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)

# if statement
# Note to  end the indentation on the if block press the shift and tab buttons
# Note elif means else if
# Note else will be executed if none of the above statements are true

temperature = 95
if temperature > 90:
    print("it's a hot day")
    print("drink plenty of water")
elif temperature > 80:
    print("it's a nice day")
elif temperature > 70:
    print("it's a bit cold outside")
else:
    print("it's a cold day")

# if statement exercise, take a number and convert it into Kilos or Pounds

weigth = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weigth / 0.45
    print("Weight in Lbs : " + str(converted))
else:
    converted = weigth * 0.45
    print("Weight in Kgs: " + str(converted))


