

# CLASS with __init__ function with User Input
class Computer:
    # __init__ is container for variables (CONSTRUCTORS)
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    

    def intel(self): # 'self' is only used if you use Instance Method
        print('CPU: {}, RAM: {}, HDD: {}'.format(self.cpu, self.ram, self.hdd))

    def ryzen(self): # 'self' is only used if you use Instance Method
        print('CPU: {}, RAM: {}, HDD: {}'.format(self.cpu, self.ram, self.hdd))

pro = input('Enter a Processor for Computer 1: ')
memo = input('Enter a RAM for Computer 1: ')
hard = input('Enter a Hard Drive for Computer 1: ')

pro1 = input('Enter a Processor for Computer 2: ')
memo1 = input('Enter a RAM for Computer 2: ')
hard1 = input('Enter a Hard Drive for Computer 2: ')

comp1 = Computer(pro, memo, hard) # Instance Method
comp2 = Computer(pro1, memo1, hard1) # Instance Method

comp1.intel()
comp2.ryzen()


# Instance & Class Variable
class pc:

    ram = '16gb' # Class Variable

    def __init__(self): # Instance Variable (present to all Objects & can be changed)
        self.cpu = 'Intel i9'
        self.hdd = '1TB'

pc1 = pc() # Instance Method
pc2 = pc() # Instance Method

pc1.cpu = 'Ryzen 3' # Only pc1 is changed
pc1.hdd = '800GB' # Only pc1 is changed
pc.ram = '8gb' # pc1 & pc2 has changed because the class variable changed

print('CPU: {}, HDD: {}, RAM: {}'.format(pc1.cpu, pc1.hdd, pc.ram))
print('CPU: {}, HDD: {}, RAM : {}'.format(pc2.cpu, pc2.hdd, pc.ram))


# Class Method
class Student:
    school = 'USTP'

    @classmethod # To know that it is Class Method not for Instance & Static method
    def student_information(cls): # Must use 'cls' not 'self'
        return cls.school

    @staticmethod # To know that it is Static Method not for Instance & Class method
    def stat():
        print('This is a Static Method')

print(Student.student_information()) # classname.method - Calling the class method
Student.stat() # Calling the static method (classname.method)



