#!/usr/bin/env python
# coding: utf-8

# # Functions
# -set of code that performs some tasks
# def func_name():
#     statemt

# In[2]:


def welcome():
    print("Good morning")

welcome() #calling a function


# In[3]:


def add(a,b):
    total=a+b
    print("the sum is ", total)
    
add(10,20)
x=2
y=3
add(x,y)


# In[6]:


def add(a,b):
    total=a+b
    print("a:%d b:%d" %(a,b))
    print("the sum is ", total)
    
add(10,20)
x=2
y=3
add(x,y)


# In[11]:


def add(*a): #a is stored as a list
    total=0
    
    for i in a:
        total += i
        print(i)
    print("The sum of the list is ", total)
   
    
add(10,20,30,50)


# In[16]:


def add(a,b):
    print("Addresses of a and b are",id(a),id(b))  #addresses of a and b
    total=a+b
    print("the sum of a and b is ", total)
    
add(10,20)
x=2
y=3
add(x,y)


# In[20]:


def add(a,b):
    total=a+b
    return total

results = add(10,20)
print("the sum is ",results)
# x=2
# y=3
# add(x,y)


# In[ ]:




