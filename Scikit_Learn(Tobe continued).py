#!/usr/bin/env python
# coding: utf-8

# # Scikit-learn
# -Simple and efficient tool for data mining and data analysis 
# 
# -Built on Numpy, SciPy and matplotLib
# -open source, commercially usable-BSD licence

# # What can we achieve in SciKit-learn
# Classification
# -Identifying which category an object belongs to
# Application: Spam detection
#     
# Regression
# -Predicting an attribute associated with an object
# 
# Application: Stock Prices prediction
# 
# Clustering
# - Automatic grouping of similar objects into sets
# Application: Customer segmentation
# 
# Model Selection
# -Comparing, validating and choosing parameters and models
# 
# Application: Improving model accuracy via parameter tuning
# 
# Dimensionality reduction
# - Reducing the number of random variables to consider 
# Application : To increase model efficiency
# 
# Pre-Processing
# -Feature extraction normalization
# -Application: Transforming input data such as text for use with machine learning algorithms

# In[3]:


#importting requred packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
#from sklearn.linear_model import SGDCClassifier
from sklearn.metrics import confussion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('pip install sklearn')


# In[ ]:




