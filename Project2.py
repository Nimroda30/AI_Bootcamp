# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZbLXcAhZBLNl-lx2xzNDipPhZVzY4nMD
"""

#print a statement
print("hello world")

print("indentation is important");
print("indentation is important")

name = "Nimroda"
print("My name is " + name)

name = "James"
age = 22
height = 2.1
is_student = True
print("My brother's name is " +name )
#print("and he is " + age + " years old")
#print("His height " + height)
#print(" is he a student? "+ is_student)

#list
person = {"name": "John", "age": 25, "is_student": True}
print("This is the variable for name: " + person['name'])
print("This is the variable for age: " + str(person["age"]))

#print(person['name'])

print("The last name typed is "+name)

#if statement
age = 19
if age <= 17:
  print("You can drive")
else:
  print("Wait until you reach " + str(age) + " to be able to drive")

#For loops
fruits = ("apple", "banana", "orange")
print("The fruits that are available in the busket are:")
for i in fruits:
  print(i)
  #print("My brother loves " + fruits[0] + " more than " + fruits[1])

#Nested for loop
fruits = ["apple", "banana"]
colors = ["red","yellow"]

for fruit in fruits:
  for color in colors:
    #print(" ");
    print("The color of " +fruits[0] + " is " + colors[0])
    print("The color of " +fruits[1] + " is " + colors[1])

    #print(fruit + " : "+ color)

#while loop
cookies = 10
#print("Enter number: " input())
while cookies > 11:
  print("Please try again")
  #print("Enter another number: "+input())
  break
else:
  print("Thats great!")

def add_numbers(a, b):
  results = a + b
  return results

results = add_numbers(5, 3)
print("The sum of 5 and 3 is "+str(results))

results = add_numbers(4, 3)
print("The sum of 4 and 3 is "+str(results))

import math

result = int(math.sqrt(25))
print(result)