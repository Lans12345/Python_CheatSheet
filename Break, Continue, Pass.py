

# Break - break the loop
stock = 5
c = int(input('How many candies do you want? '))
i = 1
while i <= c:
    if c > stock:
        print('Not Enough Stock!')
        break
    print('Candies')
    i += 1

for i in range(5):
    if i == 3:
        break
    print("Its ", i)


# Pass
for i in range(5):
    if i == 3:
        pass
    print("Its ", i)

# Continue - Skip
for i in range(5):
    if i == 3:
        continue
    print("Its ", i)