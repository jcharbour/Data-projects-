#!/usr/bin/env python
# coding: utf-8

# # Nashville Housing Data - general exploration
# 

# In[4]:


import numpy as np
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt


# ###  Reading the input file using the *pd.read_csv()* function and storing inside a panda dataframe

# In[5]:


df = pd.read_csv("nashville_housing.csv")


# In[6]:


df.head() # just to quickly view data is present in the variable.


# ### Select and show all the houses that were sold for more than 1 000 000 USD. 

# In[7]:


df[df['Sale Price'] > 1000000] #YOUR CODE HERE


# ###  Select and show all the houses that are located in Brentwood

# In[8]:


df[df['Property City'] =='BRENTWOOD'] # YOUR CODE HERE


# ###  How many houses  were sold in 2014?

# In[9]:


tmp = "xx/xx/14" # creating a formatted variable to more easily locate homes sold in 2014.


# In[10]:


tmp.endswith('14')


# In[11]:


df['Sale Date'][0]==14


# In[12]:


counter = 0
for rec in df['Sale Date']:
    if str(rec).endswith ('14'):
        counter +=1
        
print (counter)


# In[13]:


cond = df['Sale Date'].str.endswith ('14')
len(df[cond])   # 


# ##  How many houses sold in Antioch area in 2015?

# In[14]:


#select all records in Antioch... I will use the upper string method to exactly match the text in the file.
cond1 = df['Property City'].str.upper() == 'ANTIOCH'
antioch_houses = df[cond1]# dataframe

# select all the Antioch homes sold in 2015
cond2 = df['Sale Date'].str.endswith('15')
len(antioch_houses[cond2])


# In[15]:


df[cond1 & cond2] # combining the conditions to create a new dataframe.


# ###  What was the average house price in 2013?

# In[16]:


tmp = df[df['Sale Date'].str.endswith('16')]["Sale Price"] #.mean() function  and .median() for the median home price.


# In[28]:


fmt = tmp.mean()
print("The average home price in 2013 was: $",format(fmt,",.2f"))


# In[29]:


med = tmp.median ()
print("The median home price in 2013 was: $",format(med,",.2f"))


# ### What was the average price of 4-bedroom houses in the Nashville area between 2013 and 2016?

# In[31]:


cond3 = df['Property City'].str.upper () == 'NASHVILLE'
tmp   = df[cond3]

cond4 = df['Bedrooms'] == 4
tmp2  = tmp[cond4]


# In[32]:


fbdrm =tmp2['Sale Price'].mean()
print("The average price of a 4-bedroom home in the Nashville area between 2013 - 2016 was: $",format(fbdrm,",.2f"))


# ###  Remove the State, Image, and Parcel ID columns

# In[7]:


# CODE HERE
del df['State']
del df['Parcel ID']
del df['image']


# ###  Remove all records that have at least one missing value

# In[140]:


df.dropna()       # This also shows the columns mentioned above have been deleted. 


# ### How many records are left in the dataframe? 

# In[33]:


tmp5 = df.dropna()
len(tmp5)
# using the len function to find the remaining records in the dataframe. 


# In[34]:


tmp5   # a quick print of the records.


# In[ ]:




