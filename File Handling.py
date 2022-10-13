
# Reading Files
file = open('New Text Document.txt', 'r')
print(file.read()) # read the whole text
print(file.readline()) # read only one line
print(file.readline(3)) # reads only 3 characters


# Writing Files
write = open('lance', 'w') # writes the file into text file 'lance'
write.write('Lance Olana') # inside 'lance' text file, 'Lance Olana' is being write


# Appending text
app = open('lance', 'a')
app.write('ustp') # adding 'ustp' in 'lance' text file


# writing all the text in 'file' to the 'lance' text file using for loop
for data in file:
    write.write(data)