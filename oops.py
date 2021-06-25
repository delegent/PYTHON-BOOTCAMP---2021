### OBJECT ORIENTED PROGRAMMING ###

"""def f1():
    print('Hello')

def f2():
    print('Hello1')
    
f1()
f2()
#Procedural Programming
OOPs - system,structure

[Class, Object]

Main aspects
Encapsulation
Inheritance
Polymorphism
Data Hiding""

Class -
keyword
class - (data + function) - >encapsulation
has some name
defining a class = defining a type
class is a description of an object
int , float , complex, -  built in classes

Object-
Object is a example.
 (data + function) -> Object

parent
 - data
 - function

 objects""

class Test:
    i = 1
    def f1():
        print('Hello')

print(Test.i) # Test - class Object
Test.f1()
t = Test()
print(t.i)
#t.f1()
""
__init__() - > acts a constructor""

class Test:
    def __init__(self):
        print('Run')
    def f1(self):  # Class KaFUnction
        print('Hello')

t = Test() #-> Test(t)
t.f1()
""

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        sqArea = self.length * self.breadth
        print(sqArea)
    
        

s = Rectangle(5,6)
s.area()
""
Instance variables
Static variables

""
Account
AccName
AccNo.

""
Instance Variable
class Rectangle:

    ""def __init__(self,l,b): # Instance variable using INIT 
        self.length = l 
        self.breadth = b
        #self.length....braedth - instance member vaiables
        ""
    def instanceInput(self):
        self.length  = int(input("Enter the length : "))
        self.breadth = int(input("Enter the breadth : "))

    def area(self): #Instance Member FUnction
        sqArea = self.length * self.breadth
        print(sqArea)
    
        

s = Rectangle()
s.instanceInput()
s.area()
""
s2 = Rectangle(10,12)
print(id(s1))
print(id(s2))
#s.area()
""
Static Variables
Account-

""
There is no static keyword
""
class  Test:
    a = 10 #Static Variable
    def __init__(self):
        self.x = 100 # Instance Variable
        Test.b = 1200 #Static variable

""
Inheritance
OOP - Encapsulation - data + function
Car - Sports Car
Person - Student
Polygon - Triangle

Base Class,Super old Parent
Derived Class

""
class Person:
    def __init__(self,n,a):
        self.n = n
        self.a = a
    def showName(self):
        print(self.n)

    def showAge(self):
        print(self.a)
        
class Student(Person):
    def __init__(self,n,r,a):
        self.r = r
        #Person.__init__(self,"Anubhav",19)
        super().__init__(n,a)
    def showRoll(self):
        print(self.r)

n = input("Enter the Name: ")
a = int(input("Enter the age: "))
r = int(input("Enter the roll: "))
s = Student(n,r,a)
s.showName()
s.showRoll()
s.showAge()

""
Polymorphism

This is my right
turn right
You have made the right decision

poly - many
Morphs -  forms
""
class A:
    def f1(self):
        print("A- f1")

class B:
    def f1(self):
        print("B-f1")
o = A()
o.f1()
o = B()
o.f1()

""
class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("You have to make derived class")

class Dog(Animal):
    def talk(self):
        return "woof"

class Cat(Animal):
    def talk(self):
        return 'meow'

animals = [Dog("Moti"),Cat('Rani'),Dog('Facebook'),Cat('apple')]
for animal in animals:
    print(animal.name , " - ",animal.talk())

"""
# DATA HIDING
"""private
public
"""
class Test:
    i = 1234 #static variable
    __hid = 56  #hidden variable

t = Test()
print(t.i)
#print(t.__hid)
print(t.__hid)
"""
want to aces he variable  - _ClassName__variableName
"""


















