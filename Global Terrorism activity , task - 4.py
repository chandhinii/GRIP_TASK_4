#!/usr/bin/env python
# coding: utf-8

# # Importing all the libraries necessary for analysis 

# In[87]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# # Importing and reading the dataset

# In[88]:


data = pd.read_csv(r"C:\Users\USER\Desktop\globalterrorismdb_0718dist.csv",encoding='latin1')
print("Data has been successfully imported")
data.head()


# # Cleaning the dataset

# In[89]:


data.columns.values


# In[90]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City','latitude':'latitude',
    'longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound'},inplace=True)


# In[91]:


data = data[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill',
               'Wound','target1','summary','Group','Targettype','Weapon','motive']]


# In[92]:


data.shape


# In[93]:


data.isnull().sum()


# In[94]:


data['Wound'] = data['Wound'].fillna(0)
data['kill'] = data['kill'].fillna(0)


# In[95]:


data['Casualities'] = data['kill'] + data['Wound']


# In[96]:


data.info()


# In[97]:


data.describe()


# Observations
# 1. The data consists of terrorist activities ranging from the year : 1970 to 2017
# 2. Maximum number of people killed in an event : 1570
# 3. Maximum number of people wounded in an event : 8191
# 4. Maximum number of total casualities in an event : 9574

# # Visualizations of the data

# 1. Yearwise attacks 

# In[98]:


year = data['Year'].unique()
years_count = data['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,
           y = years_count,
           palette = "tab10")
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year',fontsize=20)
plt.ylabel('Number of Attacks per Year',fontsize=20)
plt.title('Attacks In Years',fontsize=30)
plt.show()


# In[99]:


pd.crosstab(data.Year, data.Region).plot(kind='area',stacked=False,figsize=(20,10))
plt.title('Terrorist Activities By Region In Each Year',fontsize=25)
plt.ylabel('Number of Attacks',fontsize=20)
plt.xlabel("Year",fontsize=20)
plt.show()


# In[100]:


attack = data.Country.value_counts()[:10]
attack


# In[101]:


data.Group.value_counts()[1:10]


# In[102]:


plt.subplots(figsize=(20,10))
sns.barplot(data['Country'].value_counts()[:10].index,data['Country'].value_counts()[:10].values,palette='Accent_r')
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation = 50)
plt.show()


# In[103]:


df = data[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4)
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# In[104]:


data['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(20,10),color='black')
plt.xticks(rotation = 50)
plt.xlabel("City",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Top 10 most effected city",fontsize=20)
plt.show()


# In[105]:


data['Attacktype'].value_counts().plot(kind='bar',figsize=(20,10),color='violet')
plt.xticks(rotation = 50)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Name of attacktype",fontsize=20)
plt.show()


# In[106]:


data[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['darkslateblue'])
plt.xticks(rotation=50)
plt.title("Number of killed ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[107]:


data[['Attacktype','Wound']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['red'])
plt.xticks(rotation=50)
plt.title("Number of wounded  ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[108]:


plt.subplots(figsize=(20,10))
sns.countplot(data["Targettype"],order=data['Targettype'].value_counts().index,palette="gist_ncar_r",edgecolor=sns.color_palette("gist_ncar_r"));
plt.xticks(rotation=90)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.title("Attack per year",fontsize=20)
plt.show()


# In[109]:


data['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='gray',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("Attack number",fontsize=15)
plt.show()


# In[110]:


data[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='pink',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("No of killed people",fontsize=15)
plt.show()


# In[111]:


df=data[['Group','Country','kill']]
df=df.groupby(['Group','Country'],axis=0).sum().sort_values('kill',ascending=False).drop('Unknown').reset_index().head(10)
df


# In[112]:


kill = data.loc[:,'kill']
print('Number of people killed by terror attack:', int(sum(kill.dropna())))


# In[113]:


typeKill = data.pivot_table(columns='Attacktype', values='kill', aggfunc='sum')
typeKill


# In[114]:


countryKill = data.pivot_table(columns='Country', values='kill', aggfunc='sum')
countryKill


# OBSERVATIONS

# 1. Regarding the attacks based on yearwise:
# 
# A) ATTACKS
#    a) Maximum number of attacks - 16903 in the year 2014
#    b) Minimum number of attacks - 471 in 1971
#    
# B)casualities
#    a) Maximum number of casualities - 85618 in 2014
#    b) Minimum number of casualities - 255 in 1971
#    
# C) Death
#    a) Maximum number of people reported dead - 44490 in 2014
#    b) Minimum number of people reported dead - 173 in 1971
# 
# D) Wounded
#    A) Maximum number of people wounded - 44043 in 2015
#    B) Minimum number of people wounded - 82 in 1971
#    
# 2. Regarding region wise attacks:
# 
# A)ATTACKS
#   a) Maximum number of attacks - 50474 in "Middle east and North Africa"
#   b) Least number of attacks - 282 in "Australiasia and oceania"
#    
# B) casualities 
#    a) Maximum number of casualities - 351950 in "Middle east and North Africa"
#    b) Minimum number of casualities - 150 in "Australiasia and oceania"
#    
# C) Death 
#    a) Maximum number of people reported dead - 137642 in "Middle east and North Africa"
#    b) Minimum number of people reported dead - 150 in "Australiasia and oceania"
#    
# D) Wounded 
#    a) Maximum number of wounded - 214308 in "Middle east and North Africa"
#    b) Minimum number of wounded - 260 in "Australiasia and oceania"
#    
#    
#  

# # Conclusion

# Terrorist acts in the Middle East and northern Africa have been seen to have fatal consequences. The Middle East and North Africa are seen to be the places of serious terrorist attacks. In addition, even though there is a perception that Muslims are supporters of terrorism, Muslims are the people who are most damaged by terrorist attacks. If you look at the graphics, it appears that Iraq, Afghanistan and Pakistan are the most damaged countries. All of these countries are Muslim countries.

# In[ ]:




