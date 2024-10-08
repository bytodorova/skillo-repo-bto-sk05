# 1. Write a Python script that prints "Hello, World!" to the console

print("Hello, World!")

# 2. Create variables to store your name, age, and favorite color. Then, print out a message using these variables (e.g., "My name is [name], I am [age] years old, and my
# favorite color is [color].").

name = 'Bogdana'
age = 34
favorite_color = 'green'

print(f"My name is {name}, I am {age} years old, and my favorite color is {favorite_color}.")

#another way

my_name='My name is Bogdana,'
my_age = 'I am 34 years old'
favorite_color = 'and my favorite color is green'

print(my_name, my_age, favorite_color)

# 3. Write a program that calculates the area of a rectangle. Prompt the user to enter the length and width, calculate the area, and then print it

length = float(input("Please, enter the length of the rectangle: "))
width = float(input("Please, enter the width of the rectangle: "))
calculate_area = length * width

print(calculate_area)

# 4. Write a program that converts temperatures from Fahrenheit to Celsius. Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent
# temperature in Celsius

fahrenheit = float(input("Please, enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 1.8

print(f"Temperature in Celsius is: {celsius}")

#  5.  Create a program that asks the user to enter two numbers and then prints out the sum, difference, product, and quotient of those numbers.

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))


sum_result = x + y
difference = x - y
product = x * y
quotient = x / y

print(sum_result)
print(difference)
print(product)
print(quotient)

#  6.  Write a program that prompts the user to enter a radius and then calculates and prints the area and circumference of a circle with that radius.

# define variable for radius and PI
radius = float(input("Enter the radius of the circle: "))
PI = 3.14

# calculation for area and circumference
area = PI * radius**2
circumference = 2 * PI * radius

print(area)
print(circumference)


#  7.  Create a program that checks whether a given number is even or odd. Prompt the user to enter a number and then print out whether it's even or odd.

number = int(input("Please, enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#  8.  Write a program that prompts the user to enter their age and then determines and prints out whether they are eligible to vote (i.e., if they are 18 or older).

user_age = (int(input("Please, enter your age: ")))
if user_age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

#  9.  Create a program that prompts the user to enter a string and then prints out the length of the string.

string = (input("Enter string: "))

string_length = len(string)

print(f"The length of the entered string is: {string_length}")


#  10. Write a program that prompts the user to enter two strings and then concatenates them together (i.e., joins them into one string) and prints out the result

string1 = str(input("Enter first string: "))
string2 = str(input("Enter second string: "))
concatenate_string = string1 + string2

print(f"{concatenate_string}")
