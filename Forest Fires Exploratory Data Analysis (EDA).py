#!/usr/bin/env python
# coding: utf-8

# # Forest Fires Exploratory Data Analysis (EDA)

# In[ ]:


### Importing Irwin Data Set which covers dates from July 31,2016  to  July 11,2019. 


# In[2]:


import pandas as pd 
import csv


# In[51]:


pwd


# In[52]:


fireinfo = pd.read_csv("combined forest fire incidents.csv",low_memory = False)


# In[91]:


# Here I am converting the data into a dataframe for a more organized look. 
fireinfo = pd.DataFrame(fireinfo) 
fireinfo.head()


# In[92]:


fireinfo.describe()


# In[93]:


# Here we can see a number descriptive data summaries which can lead to a number of preliminary genealizations 
# for furture investigation. 

# some interesting things worth noting: * 9818 fatalities  * avg initial lat(40.527867) and long (-111.807652) 
#                                       * 10355 injuries   * max of 4 fatalities per incident   * max of 69 injuries per incident

# columns to remove(count of 0) : Critical resource needs, Final fire report approved by (all 3), Fiscally responsible unit 


# In[94]:


# The shape and head functions are great for displaying the number of rows and columns present as well as the 
# columns mainly contain NaN values which will be eliminated in the next lines of code.
fireinfo.shape


# In[95]:


fireinfo.head()


# In[97]:


# Using the drop function to remove a reasonably short list of columnsis pretty efficient. It is important to include the axis you desire to remove. 
# Axis = 1 removes columns while axis = 0 removes rows. Lastly,to ensure we can display the new dataframe with deletions inline with previous,
# version of the dataframe, we conclude the statement with inplace = True.

fireinfo.drop(['Unnamed: 261','Unnamed: 262'], axis=1, inplace=True)


# In[98]:


fireinfo.head()


# In[100]:


# To quickly and easily remove a number of rows (or columns) with a high number NaN we will identify NaN's.
fireinfo.isnull().sum()


# In[102]:


# To quickly assess if we want to keep a column, we can display the percent of NaN's of each column using
fireinfo.isnull().sum()/len(fireinfo))*100


# In[110]:


# For this pass we will only use the axis and threshold parameters to select the columns with a high number of Nan's.
Fireinfo_clean = fireinfo.dropna(axis = 1, thresh = 19000)


# In[111]:


Fireinfo_clean.head()


# In[112]:


Fireinfo_clean.shape


# ### We now have cleaned the data to show the rows and columns with enough information to further explore.

# In[ ]:




