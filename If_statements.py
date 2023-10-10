#!/usr/bin/env python
# coding: utf-8

# # if condition:
#     #Statements
#     #condition

# In[1]:


a = 17
if a>18:
    print("You are an adult")
print("Your age is", a)


# In[2]:


#if_else statement
a = 17
if a>18:
    print("You are an adult")
else:
    print("You are under age")
print("Your age is", a)
    


# In[8]:


i = int(input("enter a number "))
if i%2 == 0:
    print("i is an even number")
else:
    print("i is an odd number")


# # Nested if statent(if inside if statement)
# if(cond1):
#   if(cond2):
#   cond2 here
#  cond1 ends here

# In[9]:


c=21
if c<25:
    if c%2==0:
        print("c is an even number less than 25")
    else:
        print("c is an odd number less than 25")
else:
    print("c is greater than 25")
        


# # if-elif-else statement
# if(cond1):
#   statement
# elif(cond):
#   statement
#   :
# else:
#  statement

# In[ ]:


if-elif-else ladder


# In[12]:


var = "z"
if var == 'a':
    print("This is a vowel a")
elif var == 'e':
     print("This is a vowel e")
elif var == 'i':
     print("This is a vowel i")
elif var == 'o':
     print("This is a vowel o")
elif var == 'u':
     print("This is a vowel u")
else:
    print(var, " is a consonant")


# In[ ]:




