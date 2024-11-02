# Problem 0: Create a class "Person" with a special method "__str__" to provide a string representation.Instantiate an object of this class and print it.

class Person:
  def __init__(self, first_name, last_name):

    self.first_name = first_name
    self.last_name = last_name

    person = Person('Bogdana', 'Todorova')
    print(person)
#
# Problem 1: Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses.Test the equality and inequality operators with different email instances.
#
#
#
# Problem 2: Create a class "Student" with protected attributes for name and age.Implement property getter and setter methods for these attributes.Demonstrate their usage.
#
#
# Problem 3:
# Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry. Use encapsulation to protect the account balance (it should be read-only).
# Demonstrate proper usage of the class



# Problem 4:
# Implement a class "Rectangle" with private attributes for length and width. Include special methods "__eq__" and "__lt__" to compare rectangles based on area and
# perimeter. Test the comparison operators with multiple instances.



# Problem 5:
# Design an abstract class "Vehicle" with a method "start_engine()". Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently.
# Demonstrate polymorphism by calling the method on instances of both subclasses.