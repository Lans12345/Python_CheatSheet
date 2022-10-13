
# Zipping list and converting it into Dictionaries
names = ['Lance', 'Algen', 'Dominic']
gadgets = ['Computer', 'Iphone', 'Android']
combine = dict(zip(names,gadgets))
print(combine)
# output - {'# output - [('Lance', 'Ustp'), ('Algen', 'COC'), ('Dominic', 'XU')]
#
#
# # Combining List using for loopLance': 'Computer', 'Algen': 'Iphone', 'Dominic': 'Android'}


# Combining List
names = ['Lance', 'Algen', 'Dominic']
school = ['Ustp', 'COC', 'XU']
combined = list(zip(names, school))
print(combined)
names = ['Lance', 'Algen', 'Dominic']
school = ['Ustp', 'COC', 'XU']
combined = list(zip(names, school))
for (a,b) in combined:
    print(a,b)
# output -
# Lance Ustp
# Algen COC
# Dominic XU