#Problem 0
# Write a program that takes an integer input from the user and checks if it's odd or even. Use an if-else statement to print the result

int_input = int(input("Please, enter your input as an integer: "))

if int_input % 2 == 0:
    print(f"{int_input} is even")
else:
    print(f"{int_input} is odd")

#Problem 1
# Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make use of control flow constructs like the for loop and conditional statements.

sum_of = 0

for number in range(1, 101):

    if number % 2 == 0:
        sum_of += number

print("The SUM of all even numbers from 1 to 100 is:", sum_of)

#Problem 2
#Write a Python script that prompts the user in the console a simple problem ( how much does 5 + 17 equal to ) until the user provides a correct answer.



#Problem 3
#Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.

for number in range(1, 1001):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)


#Problem 4
#Design a Python program that simulates a simple guessing game. The program should generate a random number between 1 and 100 and ask the user to guess it. Provide hints like "Too high" or "Too low" until the user guesses the correct number. Use a while loop for this game


#Problem 5
#Modify problem 2 so that every time the user is prompted the problem is different. Think of a way to design that and come up with a proper solution for that


#Problem 6
#Write a Python program that takes an integer input from the user and prints the multiplication table for that number from 1 to 10 using a for loop.

number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Problem 7
#Create a Python program that checks if a given integer is a prime number. Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime


#Problem 8 Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
#Expected output for input “5”:
#1
#12
#123
#1234
#1234

n = int(input("Enter the number of rows: "))
# range(1, n + 1)
