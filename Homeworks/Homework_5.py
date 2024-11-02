#1. Create a list with the numbers from 1 to 10 and print it.

numbers = list(range(1, 11))
print(numbers)

# 1.1. Create a list with the numbers from 1 to 1000 and print it.

numbers_t = list(range(1, 1001))
print(numbers_t)

#2. Reverse the order of the elements in the list from problem 1 and print the result.

numbers.reverse()
print(numbers)

#3. Given a list of words, create a new list contain the length of each word.

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Canberra', 'Broome', "Adelaide", 'Perth']

lengths = [len(word) for word in cities]
print(lengths)

#3.1 Given a list of words, create a new dictionary mapping every word to it's length.

print(
    {name:len(name) for name in cities}
)

#4. Write a function that takes a list and returns the sum of all even numbers in the list.

def sum_of_even_numbers(my_numbers):
    total = 0
    for num in my_numbers:
        if num % 2 == 0:
            total += num
    return total

my_numbers = [10, 12, 13, 40, 5, 6]

print(sum_of_even_numbers(my_numbers))

#5. Given a tuple of integers, find the max and min values without using built-in functions.

print(min(numbers_t))
print(max(numbers_t))


# 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue.

# Global variable for the queue
#queue = []

# 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.

students_accounts = {
    "Alex": ["653342110", "987980001"],
    "Marie": ["101066689"],
    "Nico": ["101066689"],
    "Thomas": ["404555987", "242526271", "389754210"]
}

print(students_accounts)
print("Thomas' bank accounts:", students_accounts["Thomas"])

# 8. Think of a function that can hash lists. Implement it and test it.


# 9. Write a function that counts the frequency of each word in a given string (copy the first paragraph of an online article, for example) and returns a dict with the result.

string = "Quality is more important than quantity. One home run is much better than two doubles"
word_list = string.split()

word_frequency = {}
for word in word_list:
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, count in word_frequency.items():
    print(f"{word}: {count}")


# 10. Create two sets with some common elements and find their intersection.


set_num = {10, 12, 23, 24, 25}
set_num_2 = {24, 25, 26, 37, 38}

intersection = set_num.intersection(set_num_2)

print(intersection)


# 11. Given two sets, write a function that determines if one set is a subset of the other. Do not use `<` or `>`


# 12. Write a function to remove duplicates from a list using a set.

all_nums = set_num.union(set_num_2)
print(f"{all_nums}")


# 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30.


# 14. Given a list of words, create a dictionary where the keys are the words and the values are their lengths, using dictionary comprehension.

words = ["Detroit", "Seattle", "Sacramento", "Orlando"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and sets.

