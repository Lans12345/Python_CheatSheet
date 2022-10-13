import sys
from functools import reduce

# Function with no return statement
def s(x, y):
    z = x + y
    print(z)
s(5, 10)

# Function with User input and Return statement
def name(a):
    a = input('Enter your name: ')
    return a
n = name('')
print(n)

# Function with User input and Return statement
def add(x, y):
    z = x + y
    return z
num1= int(input('Enter a numbers: '))
num2= int(input('Enter a numbers: '))
sum = add(num1, num2)
print(sum)

# Function that returns two values
def num(x, y):
    z = x + y
    v = x - y
    return z, v
num1, num2 = num(20, 40)
print(num1, num2)


# ARGUMENTS!!!
def person(name, age):
    print(name)
    print(age)
person("Lance", 19) # Proper passing of Argument
person(age=19, name="Lance") # Not Proper passing of Argument only used when you dont know the variables arguments

# only name is printed
def person(name, age = 19):
    print(name)
    print(age)
person("Lance")
# overriding age
def person(name, age = 19):
    print(name)
    print(age)
person("Lance", 20) # This 20 will override the 19

# Multiple Argument
def person(name, **data):
    print(name)
    print(data)
person("Lance", age=19, city="Bukidnon", mob='0909')

# Printing the data using For Loop
def person(name, **data):
    print(name)
    for i,j in data:
        print(i, j)
person("Lance", age=19, city="Bukidnon", mob='0909')


# GLOBAL
a = 5
def num():
    global a
    a = 10
    print(a)
num()
print(a)
# GLOBALS
a = 10
b = 2
def num():
    x = globals()['a']
    x = 20
    print(x)
    globals()['a'] = 100
num()
print(a)

# Passing List in a Function (Printing the even numbers)
x = [10, 13, 16, 18, 20]
def list():
    for i in range(0, 5):
        if i % 2 != 0:
            continue
        print(x[i])
list()

# Passing List in a Function (Printing how many numbers are Even and Odd)
lst = [12, 13, 15, 16, 18, 20, 22, 24, 26, 29]
def count(lst):
    e = 0
    o = 0
    for i in lst:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o
even, odd = count(lst)
print("Even: {}, Odd: {}".format(even, odd))


# Printing the user input if their name contains 5 Elements
def nani():
    for i in range(0, 10):
        name = input('Enter your name: ')
        if len(name) == 5:
            print("Yes!")
        else:
         print("No!")
nani()


# RECURSION (import sys needed)
print(sys.getrecursionlimit())
sys.setrecursionlimit(14) # It always -4
def rec():
    print("Hello")
    rec() # Recursion 1000 limit
rec()

# Factorial using RECURSION
def rec(n):
    if n == 0:
        return 1
    return n * rec(n - 1)
num = int(input('Enter a number you wanted to Factorial: '))
fact = rec(num)
print(fact)

# Recursion Count backwards
def count(n):
    if n == 0:
        print('Done!')
    else:
        print(n)
        n -= 1
        count(n)
        return count
n = int(input('Enter a number: '))
num = count(n)

# LAMBDA
func = lambda x, y : x + y
f = func(10, 20)
print(f)

# Using lambda in Filter(), Map(), Reduce()
nums = [2, 3, 5, 8, 9, 12]
evenNums = list(filter(lambda n : n % 2 == 0, nums)) # Printing the numbers that is even
print(evenNums)
timesTwo = list(map(lambda n : n * 2,evenNums)) # Times two the result of evenNums
print(timesTwo)
sum = reduce(lambda a,b : a + b, timesTwo) # Adding all the values in timesTwo (To use reduce import "from functools import reduce")
print(sum)