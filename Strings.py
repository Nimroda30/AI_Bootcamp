#!/usr/bin/env python
# coding: utf-8

# # Strings

# In[ ]:


stg = "Nimroda's birthday"
print(stg)


# In[3]:


stg1 = 'Nimroda\'s birthday'
print(stg1)


# In[5]:


stg2 = '''Hello, Nimroda
Welcome Home'''
print(stg2)


# In[9]:


for i in stg:
    print(i, end =" ")


# # Slicing

# In[7]:


print(stg[0:5])


# In[10]:


print(stg[5:])


# # Built-in function

# In[11]:


print(stg.upper()) #prints string in uppercase
print(stg.lower())#prints string in lowercase


# In[16]:


print(stg.find('s')) #return index
print(stg.index('s')) #return index


# In[23]:


x = stg.split(" ")
print(x)


# In[24]:


print(stg2.replace("Home","Python Tutorials"))


# In[31]:


stg3 = "Nimroda's birth month"
print(stg3)
print(stg3.rpartition(" birth "))


# # Concatenating strings

# In[32]:


x = "I"
y ="love"
z = "Python"
conc = x + " " + y + " " + z
print(conc)


# In[34]:


form = "{} {}, {}!".format(x,y,z)
print(form)


# In[ ]:




