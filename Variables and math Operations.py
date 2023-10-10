#!/usr/bin/env python
# coding: utf-8

# #Variables

# In[ ]:


x = 100


# In[ ]:


type(x) #prints the datatype of the variable


# In[3]:


y="Nimroda"
type(y)


# In[4]:


i = [5, 3, 6]
type(i)


# In[5]:


print(i[2]) #prints index 2 variable from the list


# #Tuples

# In[33]:


x = (4, 8, 6)
print(x)
type(x)


# Difference between lists and tuples is that:
# 
# Tuples are immutable, meaning they can not be changes once stored in the tuple.
# while lists are mutable, meaning the variable inside the list can be changed

# Arithmetic operations

# In[10]:


a = 2
b = 4


# In[11]:


sum = a + b


# In[ ]:


diff = b - a


# In[ ]:


mult = b * a


# In[ ]:


div = b/a


# In[14]:


res = b//a
print(exp)


# In[15]:


remainder = b%a
print(remainder)


# String Operation

# In[17]:


stringVal = "Nimroda"
print(stringVal[5:])
print(stringVal[:3])
print(stringVal[1])


# In[19]:


print(stringVal[:20])


# Conversion

# In[22]:


x = "123"
type(x)

int(x) #convert x to string

print(x)
y = 1 + x #You cant add the changed variable


# In[24]:


x = complex(x) # changes x to complex data type\
print(complex(2,5)) #function to change to complex/another way to change datatype to complex
print(x)


# math Functions

# In[29]:


a = -7.5
print(abs(x)) #absolute number(change neg to pos)


# In[30]:


#use math library before usng exp
import math
a = 10
print(math.exp(a))


# In[31]:


math.pi


# In[ ]:


print(math.sqrt(9))


# In[32]:


max(5,30,4,600)


# In[ ]:




