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



#If else statement

x = 11

if x > 18:
    print('false')
if x < 18:
    print('true')
else:
    print('equal')    

    
    
#for loop

names = ['amir', 'jack', 'kevin', 'mark', 'bob']

for x in names:
    print(x, len(x))



#Range
for x in range(0, 10):
    print(x)

for y in range(0, 100, 10):
    print(y)

print( list( range(10) ) )
print( tuple( range(10, 20) ) )


"""
#break, continue, pass

names = ['amir', 'jack', 'kevin', 'mark', 'bob']

# for x in names:
#     if x == 'jack':
#         continue
#     print(x)

# for y in names:
#     if y == 'jack':
#         break
#     print(y)

# for x in names:
#     print(x)

# else:
#     print('End...')

for x in names:
    pass 
    # or
    # ... elipsice object