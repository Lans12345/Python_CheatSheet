
# If Else Statement
num = int(input('Enter a number: '))
if num > 0:
    print('Number is positive')
else:
    print('Number is negative')



# Elif Statement
num1 = int(input('Enter first numbers: '))
num2 = int(input('Enter second numbers: '))
num3 = int(input('Enter third numbers: '))
if num1 > num2 and num1 > num3:
    print("1")
elif num2 > num2 and num2 > num3:
    print('2')
elif num3 > num1 and num3 > num2:
    print('3')
else:
    print('INVALID!')