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



#4. Write a function that takes a list and returns the sum of all even numbers in the list.

# def sum_of_even():
#     if numbers % 2 == 0:
#         return sum(numbers)
#
# print(sum_of_even())

#5. Given a tuple of integers, find the max and min values without using built-in functions.

print(min(numbers_t))
print(max(numbers_t))

