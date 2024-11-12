# 1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their sum.

with open('numbers.txt', 'r') as file:
    lines = file.readlines()

total_sum = 0

for line in lines:
    total_sum += int(line.strip())

print(f'Total is: {total_sum}')

# 2. Write a program that reads a text file, "words.txt," and counts the number of words in it.

with open("words.txt", "r") as file:
    content = file.read()
    words = content.split()

    word_count = len(words)

print(f"Number of words: {word_count}")


# 3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores this data in a CSV file called "student_scores.csv."


# 4. Write a program that reads a CSV file called "employee_data.csv," and for each employee, calculates their total salary (considering base salary and bonuses) and saves it in a new CSV file called "total_salaries.csv."

# with open("employee_data.csv", "r") as file:

# 5. Design a program that reads a JSON file containing a list of products with names and prices. Calculate the total cost of all products and display it.


# 6. Write a Python script that reads a JSON file, "contacts.json," containing contact information (name, email, phone).

import json

with open("contacts.json", "r") as file:
    contacts = json.load(file)

    for contact in contacts:
        name = contact.get('Name')
        email = contact.get('Email')
        phone = contact.get('Phone')

print(f"Name: {name}, Email: {email}, Phone: {phone}")

# 7. Create a CSV file, "student_data.csv," with student names and their corresponding JSON data containing exam scores. Write a program that reads the CSV file and calculates the average score for each student.

# with open("student_data.csv", "w") as file:

# 9. Provide an example XML file, "inventory.xml," that represents a list of products in a store. Write a Python program to read this XML file and print the names and prices of all products