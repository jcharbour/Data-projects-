#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import bs4


# In[ ]:


# This exercise is designed to recreate a chart from html scrapped from an 
# ESPN page displaying current college football standing in the ACC. 


# In[2]:


response = requests.get('https://www.espn.com/college-football/standings/_/group/1')


# In[3]:


soup = bs4.BeautifulSoup(response.content, 'html.parser')


# In[4]:


teams = soup.find_all('div', attrs={'class':'team-link'})


# In[5]:


teamlist = []
for team in teams:
    teamlist.append(str.strip(team.text))


# In[6]:


teamlist


# In[7]:


headers = soup.find_all('span', attrs={'class':'fw-medium'})


# In[8]:


headerlist = []
for header in headers:
    headerlist.append(str.strip(header.text))


# In[9]:


#headerlist


# In[10]:


Headerlist1 = headerlist[:12]
Headerlist1


# In[11]:


Headerlist2 = headerlist[12:24]
Headerlist2 


# In[12]:


start = 1
end = 24
acteams = (headerlist[start: end])

acteams.remove('')
acteams


# In[20]:


html = soup.find_all('div', attrs={'class':'Table__ScrollerWrapper relative overflow-hidden'})


# In[21]:


len(html) # this is to identify the number of tables being used 


# In[22]:


table = html[0].find('tbody') 


# In[23]:


#table


# In[24]:


data_cell = table.find_all('span', attrs={'class': 'stat-cell'}) 


# In[25]:


data_celllist = []
for data in data_cell:
    data_celllist.append(str.strip(data.text))


# In[26]:


team1 = data_celllist[:11]
dfteam1 = pd.DataFrame(team1).T


# In[27]:


team2 = data_celllist[11:22]
dfteam2 = pd.DataFrame(team2).T


# In[28]:


team3 = data_celllist[22:33]
dfteam3 = pd.DataFrame(team3).T


# In[29]:


team4 = data_celllist[33:44]
dfteam4 = pd.DataFrame(team4).T


# In[30]:


team5 = data_celllist[44:55]
dfteam5 = pd.DataFrame(team5).T


# In[31]:


team6 = data_celllist[55:66]
dfteam6 = pd.DataFrame(team6).T


# In[32]:


team7 = data_celllist[66:77]
dfteam7 = pd.DataFrame(team7).T


# In[33]:


table1 = html[1].find('tbody')


# In[34]:


data_cell1 = table1.find_all('span', attrs={'class': 'stat-cell'})


# In[35]:


data_celllist1 = []
for data in data_cell1:
    data_celllist1.append(str.strip(data.text))


# In[36]:


team8 = data_celllist1[:11]
dfteam8 = pd.DataFrame(team8).T


# In[37]:


team9 = data_celllist1[11:22]
dfteam9 = pd.DataFrame(team9).T


# In[38]:


team10 = data_celllist1[22:33]
dfteam10 = pd.DataFrame(team10).T


# In[39]:


team9 = data_celllist1[11:22]
dfteam9 = pd.DataFrame(team9).T


# In[40]:


team10 = data_celllist1[22:33]
dfteam10 = pd.DataFrame(team10).T


# In[41]:


team11 = data_celllist1[33:44]
dfteam11 = pd.DataFrame(team11).T


# In[42]:


team12 = data_celllist1[44:55]
dfteam12 = pd.DataFrame(team12).T


# In[43]:


team13 = data_celllist1[55:66]
dfteam13 = pd.DataFrame(team13).T


# In[44]:


team14 = data_celllist1[66:77]
dfteam14 = pd.DataFrame(team14).T


# In[45]:


ACC_Div = pd.concat([dfteam1,dfteam2,dfteam3,dfteam4,dfteam5,dfteam6,dfteam7,dfteam8,dfteam9,dfteam10,dfteam11,dfteam12,dfteam13,dfteam14], axis=0)


# In[46]:


ACC_Div.columns = ['W-L', 'PF', 'PA', 'W-L', 'PF', 'PA', 'HOME', 'AWAY', 'STRK', 'AP', 'USA']


# In[121]:


ACC_Div


# In[ ]:




