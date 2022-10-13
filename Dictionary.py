
n = {'Lance' : 'Boutan', 'Dominic' : 'Gwapo', 'Algen' : 'Tisoy'}
print(n['Dominic'])

print(n.keys()) # First
print(n.values()) # Second/Definition

# User Input with Dictionary
n1 = input('Enter a Person that has Iphone')
n2 = input('Enter a Person that has Android')
n3 = input('Enter a Person that has Computer')
names = {n1 : 'Iphone', n2 : 'Android', n3 : 'Computer'}
print(n1 + " has " + names[n1])
print(n2 + " has " + names[n2])
print(n3 + " has " + names[n3])

# Dictionary inside Dictionary (Iphone) / List inside Dictionary (Android)
phones = {'Iphone': {'Iphone 6': 'Algen', 'Iphone 7' : 'Bret'}, 'Android': ['Chocolate', 'Lollipop', 'Kitkat'],}
print(phones['Iphone']) # Printing the values of 'Iphone' (There is a Dictionary inside the Iphone key)
print(phones['Iphone']['Iphone 6']) # Printing 'Algen'
print(phones['Android']) # Printing the values of 'Android' (There is a List inside the Android key)
print(phones['Android'][1]) # Printing Lollipop
del phones['Iphone'] # Deleting Iphone Key and its Values
print(phones)
phones['Keypad'] = 'Nokia' # Adding Keypad key and Nokia value in it
print(phones)


# Combining Dictionaries
names = ['Lance', 'Algen', 'Dominic']
gadgets = ['Computer', 'Iphone', 'Android']
combine = dict(zip(names,gadgets))
print(combine)


