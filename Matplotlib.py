#!/usr/bin/env python
# coding: utf-8

# # MatPlotlib(plotting library for python)
# 

# -used for data visualisation
# -it provides an object-oriented API for embedding plots into application
# -designed to be as usable as matlab with an advantage of being free and open source
# -supports dozens of backends & output types
# -Application of ,atplotlib: correlation analysis of variables, outlier detection, visualising distributions, gain instant insights
# 
# (Open source drawing library which supportsrich drawing types)

# It is used for 2D and 3D graphics, you can understand your data easily by visualizing it with the help of matplotlib.
# Types: histograms, bar charts, 

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


np.random.seed(10)


# In[7]:


N =30
x= np.random.rand(N)
y=np.random.rand(N)
colors = np.random.rand(N)


# In[8]:


area = (30 * np.random.rand(N))


# In[11]:


plt.scatter(x,y, s=area, c=colors, alpha =0.4)
plt.show()


# In[12]:


from matplotlib import style
style.use('ggplot')

x = [2,4,6]
y =[12,14,16]

x2 = [3,3,4]
y2 = [7,14,5]


# In[13]:


plt.bar(x,y,color='r', align = 'center')
plt.bar(x2,y2,color='b', align = 'center')

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[4]:


from matplotlib import pylab
print(pylab.__version__)


# In[10]:


"""Use Numpy to generate random data"""
import numpy as np

x = np.linspace(0,10,25)
y = x * x + 2
print(x)
print(y)
print 


# In[12]:


#draw a graph
pylab.plot(x,y, 'r')  #'r' stands for red


# In[13]:


#Drawing a subgraph

pylab.subplot(1,2,1) #The contents of the brackets represent (rows, columns, indexes)
pylab.plot(x,y,'r--') #3rd parameter represents color and line style
pylab.subplot(1,2, 2)
pylab.plot(y, x, 'g*-')


# In[14]:


fig, axes = plt.subplots(nrows= 1,ncols = 2 ) #Submap is of 1 row, 2 columns
for ax in axes:
    ax.plot(x,y, 'r')


# In[30]:


fig, ax = plt.subplots(dpi=100)

ax.plot(x, x+1, color = "blue", marker = '0')
ax.plot(x, x+2, color = "blue")


# In[31]:


fig, axes = plt.subplots(dpi=90)
axes.plot(x, x**2, color = "blue", alpha = .3)
axes.plot(x, x+6, color = "red", alpha = .3)
axes.plot(x, x+3, color = "green", alpha = .3)


# In[32]:


"""Set the canvas grid and axis range"""
fig, Axes = plt.subplots(1,2, figsize=(10,5))

Axes[0].plot(x,x**2,x, x**3,lw=2)
Axes[0].grid(True)

Axes[1].plot(x,x**2,x,x**3,lw=2)
Axes[1].set_ylim(0,60)
Axes[1].set_xlim(2,5)


# # Other 2D Graphics

# In[36]:


n = np.array([0,1,2,3,4,5])

fig, axes = plt.subplots(1,4, figsize=(16,5))
axes[0].set_title("scatter")
axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))

axes[1].set_title("step")
axes[1].step(n, n**2, lw=2)

axes[2].set_title("bar")
axes[2].bar(n, n**2, align="center", alpha=0.5)

axes[3].set_title("fill_between")
axes[3].fill_between(x,x**2, x**3, color="green", alpha=0.5)


# In[38]:


"""Draw a radar chart"""

fig = plt.figure(figsize=(6,6))
ax= fig.add_axes([0.0, 0.0, 1, 1], polar = True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t,t*2, color = 'blue', lw=3)


# In[44]:


"""Draw a histogram"""
n = np.random.randn(100000)
fig, axes = plt.subplots(1,2, figsize=(12,4))
axes[0].set_title("Default histogram")
axes[0].hist(n)

axes[1].set_title("Cumulative detailed histogram")
#axes[1].hist(n, cumulative=True, bins=50)

axes[1].hist(n, cumulative=True, bins=10)


# In[48]:


"""Draw a contour image/map"""

import matplotlib.cm as cm #colour maps
import numpy as np
import matplotlib.pyplot as plt

delta = 0.025
x = np.arrange(-3.0, 3.0, delta)
y = np.arrange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x,y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 -Z2) * 2

print(X)
print(Y)


# In[52]:


fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('contour map')


# In[ ]:




