# Problem 0:
#  Complete the following function so that it returns the sum of the elements in the list passed as an argument. Call your function several times in order to test it
#  def sum_elements(arr):
#  result = 0
#  #insert code here
#  return result

def sum_elements(arr):
    result = 0
    for element in arr:
        result += element
    return result

print(sum_elements([10, 15, 20, 25, 30]))



#  Problem 1: Simple Calculator Function
#  Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*', or '/') as arguments and returns the result of the operation.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
operator = input('+' or '-' or '*' or '/')

def simple_calculator(num1, num2, operator):

    if operator == '+':
     return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
     return num1 * num2
    elif operator == '/':
        if num2 != 0:
         return num1 / num2

result = simple_calculator(num1, num2, operator)
print (result)


#  Problem 2: Area of Shapes
#  Create a module named `geometry` with functions to calculate the area of common shapes like a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of different shapes. You should be able
# to use the function for calculating the area of a rectangle to calculate the area of a square by passing in only one argument.



#  Problem 3: Temperature Conversion
#  Write a program that converts temperatures between Celsius and Fahrenheit. Create two functions, one for each conversion, and use them in a program to convert temperatures provided by the user. Write another script which
# tests these functions.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9



#  Problem 4: Factorial(again):
#  Write a recursive function which computes the Factorial of a given integer.

def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter your number: "))
print(f"The factorial of {number} is {factorial(number)}")

# Problem 5: Online Shopping Cart
#  Create a Python program that simulates an online shopping cart using a global dictionary variable. Every customer has unique id as a key. Define functions to add items to the cart, remove items, calculate the total price, and
# display the contents of the cart. Allow the user to interact with the cart by adding and removing items.


#  Problem 6: Use Python’s built-in `os` module to explore your computer
#  # Look online for some documentation, find out what you can do with the `os` module and improvise