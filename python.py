""" 
#lists 
 
names = ['sarah', 'john', 'mark']

names2 = ['wolf', 'lion']

names.append('margot')

print(names)

print(names2)

print(names + names2)

names[1:2] = []

print(names)

print(len(names + names2))


#While loop

x = 0

while x < 10:
    print(x, end=', ') 
    x = x + 1

print('Done')

"""

#If else statement

x = 11

if x > 18:
    print('false')
if x < 18:
    print('true')
else:
    print('equal')    