from abc import ABC, abstractmethod

# INHERITANCE!!!!
class Car: # Parent Class

    def run(self):
        print('Running. . . . .')

    def stop(self):
        print('Stopping. . . . .')

class Car1: # No Inheritance

    def specs(self):
        print('Lamborghini Aventador, 500 hp')

class Car2(Car, Car1): # Multiple Inheritance (parents class)
    def specs(self):
        print('Ferrari La Ferrari, 480 hp')

c1 = Car1() # No Inheritance
c1.specs() # Printing specs of Car1
c2 = Car2() # Inherits Car & Car1
c2.specs() # Printing specs of Car2
c2.run() # Printing run method in class Car
c2.stop() # Printing stop method in class Car


# Super keyword in Inheritance
class Car: # Parent Class

    def __init__(self):
        print('In Car class.')

    def run(self):
        print('Running. . . . .')

    def stop(self):
        print('Stopping. . . . .')


class Car1: # No Inheritance

    def __init__(self):
        print('In Car1 class.')

    def specs(self):
        print('Lamborghini Aventador, 500 hp')

class Car2(Car, Car1): # Multiple Inheritance (parents class)

    def __init__(self):
        super().__init__() # Only calling the __init__ method of Car class. You cannot access the __init__ int Car1
        print('In Car2 class.')

    def specs(self):
        print('Ferrari La Ferrari, 480 hp')

c2 = Car2()


# Duck Typing (Polymorphism - method "execute"(Laptop) from different class)
class lenovo:
    def execute(self):
        print('Lenovo, 6gb, Intel core i3')

class samsung:
    def execute(self):
        print('Samsung Galaxy S10, Ryzen 3')

class Laptop:
    def code(self, model):
        model.execute() # Calling the execute methods from any class

lap = Laptop() # Instance of class Laptop
len = lenovo() # Instance of class lenovo
sam = samsung() # Instance of class samsung

lap.code(len) # Passing and Printing the lenovo class and its "execute" method in Laptop "code" method
lap.code(sam) # Passing and Printing the samsung class and its "execute" method in Laptop "code" method


# Operator Overloading (Polymorphism) - used because you cannot perform an operation in objects to objects
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1 # Adding the m1 of __init__ and m1 of this method named "other"/other objects to be created
        m2 = self.m2 + other.m2 # Adding the m2 of __init__ and m2 of this method named "other"/other objects to be created
        s3 = Student(m1, m2) # creating s3 object with the values of m1 and m2 of any objects
        return s3

    def __gt__(self, other): # Finding the greater than
        s1 = self.m1 + self.m2 # finding the total mark of __init__ method and putting it into s1 object
        s2 = other.m1 + other.m2 # finding the total mark of this method and putting it into s2 object
        if s1 > s2: # Finding the greater than
            return True
        else:
            return False

    def __str__(self): # Printing the values not the memory address of objects s1, s2
        return '{} {}' .format(self.m1, self.m2) # to be printed (values) without the brackets


s1 = Student(90, 80) # Instance of s1 and passing some values
s2 = Student(70, 80) # Instance of s2 and passing some values

s3 = s1 + s2 # (object of s3) -  Not working if added directly so must create __add__ method just like above
print(s1.m1 + s1.m2) # printing the total values of s1
print(s2.m1 + s2.m2) # printing the total values of s2
print(s3.m1 + s3.m2) # printing the total values of s1 and s2 combined

if s1 > s2: # not working if finding the greater than values so must create a __gt__ method just like above
    print('s1 wins.')
else:
    print('s2 wins.')

print(s1) # printing the values of s1
print(s2) # printing the values of s2


# Method Overriding
class Student: # Same methods, different implementation
    def ako(self):
        print('Lance Olana')
    def ako(self):
        print('Elon Musk')

stud = Student() # Instance of Student class
stud.ako() # the last "ako" method is being called

# Exception Handling
try: # Try block
    num = int(input('Enter a number: '))
    print(num)
except: # Except block (put "Exception as e" if want to print the exception type/message)
    print('Enter a number!')
finally: # Finally block (executed both ways)
    print('Done')


# 'with' Statement (much simplier to use because you dont have to close the 'f'/write variable)
with open('code.text', 'w') as f:
    f.write('hello world!')


# Abstract
# need to import - from abc import ABC, abstractmethod
# Reminder: You need to implement all the abstract methods in the abstract class
class Iphone(ABC):

    @abstractmethod
    def sendText(self): # abstract method
        pass

    @abstractmethod
    def call(self): # abstract method
        pass


class Iphone5(Iphone): # extending the 'Iphone' abstract class

    def sendText(self): # defining the abstract class 'sendText'
        print('Sending text.')

    def call(self): # defining the abstract class 'call'
        print('Calling.')


cp = Iphone5() # object of Iphone 5, you cannot create object of Iphone because it is abstract
cp.sendText() # calling the 'sendText' method
cp.call() # calling the 'call' method









