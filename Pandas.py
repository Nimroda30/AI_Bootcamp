#!/usr/bin/env python
# coding: utf-8

# # Pandas(Python Data analysis library)

# -used for data analysis cleaning 
# - It provides fast, flexible and expressive data structure designed to work with structured data easily and intuitevely
# Application of pandas: general data wrangling, etl jobs &data storage, used in wide variery and commercial domain including statistics etc, time series-specific functionality
# 
# - It is a tool for data processing which helps in data analysis
# -it provides functions and methods to efficiently manipulate large datasets
# 
# -it is a dataframe(like excel spreadsheet)

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


df =pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'))
df


# In[13]:


df.describe()


# # Series create, manipulate, query, delete

# Series(one-dimensional array with labels)
# -it can contain any data type including integers, strings, floats, Python objects and more.
# 
# DataFrame(two-dimensional data structure array with labels, we can use them to locate data)
# - 

# In[17]:


#creating a series from a list
arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)
s1


# In[19]:


order = [1, 2, 3, 4,5]
s2 = pd.Series(arr, index = order)
s2

#index data


# In[20]:


import numpy as np
n=np.random.randn(5) #create a random ndarray
index = ['a', 'b', 'c', 'd', 'e']
s2 = pd.Series(n, index=index)
s2


# In[21]:


#create series from a dictionary

d = {'a':1,'b':2,'c':3,'d':4,'e':5}
s3 = pd.Series(d)
s3


# In[27]:


#you can modify the index of series
#print(s1)
s1.index = ['A','B','C','D','E']
s1


# In[28]:


#slicing
a = s1[:3]
a


# In[30]:


b = s1[-2:]
b


# In[32]:


s4 = s1.append(s3)
s4


# In[33]:


s4.drop('e')
s4


# # Create DataFrame 

# In[5]:


import pandas as pd
import numpy as np
#import time

dates = pd.date_range('today',periods=6) #Define time sequence as index
num_arr=np.random.randn(6,4) #import numpy random array
columns =['A', 'B', 'C', 'D'] #Use the table as the column name

df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
df1


# In[9]:


data = {'animal':['dog', 'cat','snake' ],
       'age':[2.5, 3.0, 0.5]}
labels = ['a','b','c']
df2 = pd.DataFrame(data, index=labels)
df2


# In[ ]:




