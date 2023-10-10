#!/usr/bin/env python
# coding: utf-8

# # Lists 
# collection of data, it can hold values of different data types

# In[1]:


num =[2,3,4,5]
print(num)


# In[10]:


mix = [1,3,'Simple', 'get', -1, 6, 9.8]
print(mix)


# In[11]:


print(mix[::2]) #print second element from 1st element 
print(mix[::-1 #print from the end


# In[6]:


mat =[[1,2], ['a','b']]
print(mat)
print(mat[0])



# In[7]:


print(mat[-1]) #count from the end of the list


# # Operations on lists

# In[12]:


#conc 2 lists
conc = mix + num
print(conc)


# In[13]:


var = list("hey there")
print(var)


# Methods in lists

# In[14]:


#Append = add elem at the end of existing list
print(num)
num.append(8)
print(num) 


# In[15]:


#used like concatination, at the end of the string
num.extend(mix)
print(num)


# In[16]:


#insert
num.insert(5,"name")
print(num)


# In[19]:


letters = ['g','a','c', 'b', 'd', 'e','i']
letters.sort()
print(letters)


# # Build-in function in list

# In[21]:


x = [7,0,5,4,9,2]
len(x)


# In[ ]:


sum(x)


# # Tuples
# collection of immutable heterogeneous python objects. 

# In[23]:


emp = ()
print(type(emp))


# In[28]:


city = "Pune",  #the comma after the name specify that it is a tuple
type(city)
print(city)
_city = ("Polokwane", "Johannesburg", "Thohoyandou")
print(_city)
print(_city[2])


# In[ ]:


#In list we use append to add elements to the list, but we cannot add any element to tuples because they are immutable, 
#therefore tuples remain the same until the end. They can not be modified but can be concatinated
#List uses square brackets and tuples may or may not use parentheses


# In[30]:


conc = city + _city
print(conc)


# In[31]:


#Nesting tuple = tuples inside a tuple
nest = (city, _city)
print(nest)


# In[32]:


#Repetition: does not modify the tuple, it repeates the tuple 5 times
rep = city*5
print(rep)


# In[39]:


#Slicing
num = 1, 2, 3, 4

num[:2]



# In[35]:


num[::-1] #print everything in reverse


# In[36]:


num[:-1] #print everything excl the last elem


# In[37]:


#Unpacking
tuple("Ilovepython")


# In[44]:


#numList = 1,2,3,4
#print(numList)
a, b, c, d = num
print(a, b, c, d)


# In[47]:


#if you dont know the length of your variables
a,*b,c =num  
print(a,b,c) #stores the middle elements in a list as *b indicated list


# In[48]:


#Deleting a tuple
tuple1 =(1,2,3,4)
print(tuple1)


# In[49]:


del tuple1


# In[50]:


print(tuple1)


# # Built in function in tuples

# In[52]:


tuple1 =(1,2,3,4,2,2,2)

tuple1.count(2)


# In[53]:


sum(tuple1)


# # Converting list to tuple

# In[54]:


lst = [1,2,3,4]
print(lst)


# In[56]:


print(type(lst))


# In[57]:


tpl = tuple(lst) #Changing list to a tuple, but since tuple can not be modified, you can not change tuple to a list
print(tpl)
print(type(tpl))  


# # Nesting tuples in a list

# In[58]:


lst = [(1,2,3),(4,5,6)]  #storing tuples in one list
print(lst)


# In[59]:


lst.append(("Tuple1", "inside", "list")) #adding another tuple to a list
print(lst)


# In[60]:


print(type(lst))


# In[64]:


lst.remove((1,2,3)) #deleting first tuple from a list
print(lst)


# # Nesting List within tuples

# In[62]:


tpl =(['a', 'b', 'd'], ['d','e','f'])
print(tpl)


# In[63]:


tpl[0].append('z') #Even though Tuples are immutable but you can modify the list inside the tuple
print(tpl)


# In[66]:


tpl[1].append('y')
print(tpl)


# In[67]:


tpl.append([1,2,4]) #This gives error because you cannot modify tuples


# In[ ]:




