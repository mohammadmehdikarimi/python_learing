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




#Function

# def show():
#     print('Hello, World!')

# def show(name, age):
#     print('Hello ' + name)
#     print('you are ' + age + ' years old')

# def show(name):
#     return 'Hello ' + name

# x = show('john')

# print(x)

# or

# print(show('john))





#  list methods

names = ['amir', 'jack', 'kevin', 'mark', 'jack']

names.append('sarah')

names.extend(['bob', 'jane', 'john'])

names.insert(2, 'jonathan')

names.remove('jack')

# names.pop(0)  /   remove and also returns the value

print(names)




#  tuple

names = ('amir', 'jack', 'kevin', ['anna', 'bob', ('brad', 'john')])

numbers = (11, 22, 45,(15, 18, 16))


print(names)
print(numbers)



#  set / unordered , no reapeat , sensetive to capital alphabet , unmuteable

names = {'amir', 'kevin', 'jack'}

if 'amir' in names:
    print('yes')

letters = set('mongard')

print(letters)


# dictionaries / key:value pair

ages = {'amir':20, 'jack':15, 'kevin':30}

ages['anna'] = 43

ages['jack'] = 14

del ages['amir']

print(ages)

print(ages.items())

for i, j in ages.items():
    print(i, j)


# formatted string literals

name = 'jack'

age = 34

print(f'{name} is {age} years old.')




# the string format() method


# name = 'jack'

# age = 34

# print( '{} is {} years old.'.format(name, age) )
# print( '{} is {} years old.'.format('amir', 22) )

info = {'name':'jack', 'age':12}
info2 = {'name':'anna', 'age':16}

print('{0[name]} is {0[age]} years old {1[name]} is {1[age]} years old.'.format(info, info2))



# reading and writing files 

with open('text.txt') as f:
    print(f.read())



# f = open('text.txt', 'r')

# print(f.read())

# f.close()




# scope

a = 10  # global scope

def show():
    b = 30       # local scope
    print(a)


show()



# oop


class Car:   #blueprint
    pass


a = Car()    #object or instance
b = Car()


a.name = 'Benz' # attribute / property
b.name = 'Bmw'

a.price = 100000
b.price = 120000

print(a.price)

print(f'{a.name} costs {a.price}')
print(f'{b.name} costs {b.price}')



# method

class Car:   
    def __init__(self, n, p):      #built-in method
        self.name = n
        self.price = p

    def show(self):
        print(f'{self.name} costs {self.price}')


a = Car('Benz', 100)   
b = Car('Bmw', 120)


a.show()
b.show()



#variable ==> 1.instance, 2.class

class Car:   
    wheel = 4 # class variable / accesable from all variable instances
    def __init__(self, n, p):      #built-in method
        self.name = n
        self.price = p
        print(f'{self.name} costs {self.price} and has {self.wheel} wheels')
        


a = Car('Benz', 100)   
b = Car('Bmw', 120)


# method ==> 1.instance, 2.class, 3.static

import datetime

class Person:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.heght = height
        self.age = age

    def show(self):
        print(f'{self.name} is {self.heght} cm tall and {self.age} years old.')

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod
    def is_adult(age):
        if age > 18:
            print('Yes')
        else:
            print('No')


p1 = Person.from_birth('sarah', 170, 1990)

p1.show()

Person.is_adult(23)


# inheritence

class Car:              #parent / superclass
    wheel = 4
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
        print(f'i have a {self.name}')


class Motor(Car):       #child / subclass
    wheel = 2

    def show(self):
        super().show()
        print(f'i ride a {self.name}')


a = Motor('Honda')

a.show()




# python built-in methods

class Car:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def show(self):
        print(f'i have a {self.name}')

    def __str__(self) -> str:
        return f'{self.name}, {self.price}'
        
    def __add__(self, other):
        return self.price + other.price
    
    def __len__(self):
        return len(self.name)


a = Car('Benz', 100)
b = Car('Bmw', 200)

print(a)
print(a + b)
print(len(b))


"""

# access points ==> public, protected, private

class Person:
    name = 'john' #public
    _age = 32        #protected
    __height = 180       #private


class Male(Person):
    def show(self):
        # print(self._age)
        print(self.__height)


# a = Male()
# a.show()


p = Person()

print(p._Person__height)  #name mangling











