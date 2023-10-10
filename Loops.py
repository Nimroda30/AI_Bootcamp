#!/usr/bin/env python
# coding: utf-8

# # While Loop
# -is used to repeat a section of code an unknown number of times until a specific condition is met

# In[2]:


val = int(input("Enter a multiple of 7: "))

while val%7 != 0:
    val = int(input("Enter a multiple of 7: "))
else:
    print("%d is a multiple of 7" %val)


# In[26]:


i = 1
while i<=10 :
    print("PythonTutorials")
    i+=1


# In[52]:


n =int(input("Enter a number "))
i=1
while i<=n :
    j=1
    while j<=i:
        print(i,end='')
        j+=1
    i+=1
    print()


# In[55]:


#random numbers
import random
nump = random.randint(1000,9999)
n = int(input("Enter a 4 digit number"))

while n != 10:
    num = nump
    cor = 0
    while num%10 :
        numc = num%10 #last digit
        nc =n%10
        num = num//10
        n=n//10
        if numc==nc:
            cor =cor+1
    if cor ==4:
        print("Congrats, you guesses it right")
        break
    else:
        print("%d digit were guessd right" %cor)
        n=int(input("Enter a 4 digit number"))
else:
    print("You quit the game")


# # For Loop
# -used to iterate over a sequence, which could be a list, tuple, array or a string

# In[ ]:


lst = [[1,2,3],['a','b','c'],["Python","Loop"]]

for i in lst:
    for j in i: #iterate through the main list
        print(j,end ="") #iterate through each list
    print() #print on the next line


# In[3]:


x = [1, 6,"Python"]
for i in x:
    print(i)


# In[4]:


y = "Python"
for i in y:
    print(i)


# In[21]:


sum = 0
for i in range(0,21,2): #print every second element
    if i%2==0:
        sum=sum+i
    print(sum)


# # Nested Loops
# loop within loop

# In[40]:


x = [[1,2,3],['a','b','c']]
for i in x: #used to iterate through first list
    for j in i: #used to iterate through all the list
        print(j,end="") #prints both lists as one
    print()


# In[36]:


x = [[1,2,3],['a','b','c']]
for i in x: #used to iterate through first list
    for j in i: #used to iterate through second list
        print(j, end ="")


# # Loop control statements
# BREAK: Transfers control to the statement right after the loop
# -Loop control statements alter the regular flow of a loop
# -continue: skips the statements following it and return control to the beginning of the loops

# In[17]:


#Break
a = "Hey there how are you?"
for i in a:
    if i == ".":
        break
    print(i,end="")


# In[18]:


#Continue
for i in [1,13,56,10,5,6] :
    if i>10:
        continue
    print(i)


# In[41]:


for i in range(0,21,2): #print multiple of 2 from 0
    print(i)


# In[49]:


sum = 0
for i in range(0,21): #print multiple of 2 from 0
    if i%2 == 0 :
        sum =  sum + i
print(sum)


# In[ ]:




