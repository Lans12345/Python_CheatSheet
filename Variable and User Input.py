import
# eval method
exp = eval(input('Enter a numbers to solve: '))
print(exp)

# user input
name = input("Enter a Name: ")
school = input("Enter a School: ")
course = input("Enter a Course: ")
age = input("Enter age: ")
print("Hi, my name is " + name + ". I study in " + school + ", taking a " + course + " Course."
      "And I am " + age + " years old.")

# Getting the first character only
input = input('Enter your Gender: ') [0]
print('Gender: ' + input)

#__name__
# This code only printed if this file will be execute even if its been imported to other file
def name():

      print('Hello')

if __name__ == '__main__':
      name()
