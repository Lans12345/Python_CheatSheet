

# While Loops with If Else - Not printing the number 0 - 100 that is divisible by 3 or 5
a = 1
while a <= 100:
    if a % 3 == 0 or a % 5 == 0:
       pass
    else:
        print(a)
    a = a + 1

# While Loops - Printing Patterns
a = 1
while a <= 4:
    print('# # # #')
    a += 1

name = input('Enter your name: ')
num = int(input('How many times do you want to print it? '))
a = 1
while a <= num:
    print(name)
    a += 1

# For Loops - Printing all type of element in array
x = ['Lance Olana', 19, 'USTP']
for i in x:
    print(i)

# Printing Range
for i in range(0 , 11):
    print(i)

# Printing reverse order in range
for i in range(21, 0, -1):
    print(i)

# Printing in range with the element 5
for i in range(0, 101, 5):
    print(i)

# Putting User Input in the array
name = input('Enter your name: ')
name1 = input('Enter your name: ')
name2 = input('Enter your name: ')
names = [name, name1, name2]
for i in names:
    print(i)


# For Else - Printing value that is divisible by 5
x = [1, 3, 6, 10]
for i in x:
    if i % 5 == 0:
        print(i)
        break
else:
    print('Number not Found')


# Fibonacci Sequence
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
num = int(input('Enter a number range: '))
fib(num)