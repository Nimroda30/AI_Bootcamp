#!/usr/bin/env python
# coding: utf-8

# # objects and classes
# objects - everything instance in python
# class -blueprint of similar objects

# In[5]:


class Person:
    def __init__(self,n,g,a): #define constructor, n=name,gender,age
        self.name = n #self is ref
        self.gender = g
        self.age = a
        
    def talk(self): #method
        print("Hi i'm ",self.name)
        
    def vote(self):
        if self.age<18:
            print("I am not eligible to vote")
        else:
            print("I am eligeble to vote")
    
obj1 = Person("Nimroda","Female",25)
obj2 = Person("Alison","Female",17)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()


# # Object orientated Programming(OOPs)
# -Programming paradigm that focuses on objects
# -every instance in python is object
# -Object has attributes and behaviour
# attribute:data describing the object e.g. years of manufacture maximum speed
# behaviour: methods on the attributes e.g display speed 
# ,change speed
# 
# object :bmw
# class: car

# In[12]:


class car:
    def __init__(self,year,speed):
        self.year = year
        self.speed = speed
    
    def getSpeed(self):
        print("maximum speed is: ",self.speed)
    def setSpeed(self,speed):
        self.speed = speed
        
BMW = car(2018,155)
FORD = car(2016,140)

#car.getSpeed(BMW)
#car.getSpeed(FORD)

BMW.getSpeed()
#FORD.getSpeed()
BMW.setSpeed(143)
BMW.getSpeed()


# # Inheritance
# -Mechanism for a new class to use features of another class

# In[17]:


class Sedan(car): #child class
    def accelerate(self):
        print('137')
    def openTrunk(self):
        print('trunk has been opened')

class SUV(car): #child class
    def accelerate(self):
        print('127')
        
Honda = Sedan(2018,150)
BMW.getSpeed()
Honda.getSpeed()
BMW.getSpeed() 
Honda.openTrunk()
Honda.accelerate()


# # Encapsulation
# -The feature of preventing data from direct access is called encapsulation

# # Polymorphism
# is the feature of using the same function in multiple ways
