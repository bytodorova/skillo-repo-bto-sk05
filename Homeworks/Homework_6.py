# Problem 0: Create a class "Person" with a special method "__str__" to provide a string representation.Instantiate an object of this class and print it.

class Person:
  def __init__(self, first_name, last_name):

    self.first_name = first_name
    self.last_name = last_name

    person = Person('Bogdana', 'Todorova')
    print(person)

# Problem 1: Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses.Test the equality and inequality operators with different email instances.

  class Email:
    def __init__(self, address):

      def __eq__(self, other):
        if isinstance(other, Email):
         return self.address == other.address
        return False

      def __ne__(self, other):
       return not self.__eq__(other)


      email_1 = Email("b.todorova@mail.com")
      email_2 = Email("b.todorova@gmail.com")


      print(email_1 == email_2)


# Problem 2: Create a class "Student" with protected attributes for name and age.Implement property getter and setter methods for these attributes.Demonstrate their usage.

class Student:
  def __init__(self, name, age):
    self._name = name  # Protected attribute
    self._age = age  # Protected attribute

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, new_age):
    if new_age > 0:
      self._age = new_age
    else:
      raise ValueError("Positive values only!")


student = Student("Thomas", 20)
print([student.name , student.age])




# Problem 3: Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry. Use encapsulation to protect the account balance (it should be read-only).
# Demonstrate proper usage of the class



# Problem 4: Implement a class "Rectangle" with private attributes for length and width. Include special methods "__eq__" and "__lt__" to compare rectangles based on area and
# perimeter. Test the comparison operators with multiple instances.



# Problem 5:
# Design an abstract class "Vehicle" with a method "start_engine()". Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently.
# Demonstrate polymorphism by calling the method on instances of both subclasses.




# Problem 6:
# Implement a class "Book" with special methods "__str__" and "__len__" to provide a string representation and the number of pages. Create instances of "Book" and
# demonstrate the use of these methods



# Problem 7:
# Create a class "Animal" with a special method "__init__" that sets a species attribute. Implement subclasses "Dog" and "Cat" with their own "__str__" methods. Use
# polymorphism to display species information.


# Problem 8: Design a class "Employee" with encapsulated attributes for name and salary. Implement a subclass "Manager" that inherits from "Employee" and includes an additional attribute for the department.


# Problem 9:
# Create a class called "Employee" that has attributes name, start_date, PIN, phone, address, manager_name, department. Implement methods to calculate employee tenure,
# and business card info representation.


# Problem 10:
# Create an abstract class "Employee" with attributes for name and salary. Implement a subclass "Manager" that inherits from "Employee" and includes an additional
# attribute for the department. Ensure that the "Employee" class enforces encapsulation. Every employee and manager should have a method to send a message to. The
# message must be stored. Create a class "Team" that has a manager and a list of members. Implement a method that sends a message to everyone in the team

