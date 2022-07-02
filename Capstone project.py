#!/usr/bin/env python
# coding: utf-8

# 911 Capstone Project

# In this project a dataset from kaggle was analyzed, on Emergency 911 calls

# In[49]:


#importing important mathematical and visualization libraries
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#read the 911 csv
df = pd.read_csv('911.csv')


# In[4]:


#to get a brief description of your dataframe that includes datatypes, index(rows) and column
df.info()


# In[5]:


#dataframe head
df.head()


# In[6]:


#Questions
#top 5 zip code for 911 calls
df['zip'].value_counts().head(5)


# In[7]:


#top 5 townships in the dataset
df['twp'].value_counts().head(5)


# In[13]:


#number of unique titles in the title column
len(df['title'].unique())
df['title'].nunique()


#  In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.**
# 
# For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. *

# In[17]:


df['reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[22]:


#most common 'reason' for 911 calls
df['reason'].value_counts()


# * Now use seaborn to create a countplot of 911 calls by Reason. **

# In[24]:


sns.countplot(x = 'reason', data = df, palette = 'viridis')


# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

# In[26]:


type(df['timeStamp'].iloc[0])


# * You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects. **

# In[28]:


#to convert the column of datetime from strings to objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[29]:


df.head()


# In[38]:


time = df['timeStamp'].iloc[0].
time
#to confirm the change


# You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.

# In[41]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[42]:


df.head()


# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
# dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[44]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# In[45]:


df.head()


# In[ ]:





# In[54]:


sns.countplot(x = 'Day of Week', data= df, hue = 'reason', palette = 'viridis')
#relocate the legend outside
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad = 0.)


# Now do the same for Month:

# In[56]:


sns.countplot(x = 'Month', data= df, hue = 'reason', palette = 'viridis')
#relocate the legend outside
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad = 0.)


# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **
# 
# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

# In[75]:


byMonth = df.groupby('Month').count()


# In[83]:


byMonth


# In[82]:


byMonth['title'].plot()


# In[80]:


sns.countplot(x = 'Month', data= df,palette = 'viridis')
#relocate the legend outside
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad = 0.)


# In[84]:


#reset the index to add Month back as a number of coulumn
sns.lmplot(x = 'Month', y = 'twp', data = byMonth.reset_index())


# *Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. *

# In[87]:


t = df['timeStamp'].iloc[0]


# In[88]:


type(t)


# In[89]:


df['Date'] = df['timeStamp'].apply(lambda x: x.date())


# In[90]:


df.head()


# In[101]:


#group data by date dna plot against the latitude of calls made
df.groupby('Date').count()['lat'].plot(figsize = (10,5))
plt.tight_layout()


# In[103]:


#recreate for the Traffic, EMS and Fire 'reasons'
df[df['reason'] == 'Traffic'].groupby('Date').count()['lat'].plot(figsize = (10,5))
plt.title("Traffic")
plt.tight_layout()


# In[106]:


df[df['reason'] == 'Fire'].groupby('Date').count()['lat'].plot(figsize = (10,5))
plt.title("Fire")
plt.tight_layout()


# In[107]:


df[df['reason'] == 'EMS'].groupby('Date').count()['lat'].plot(figsize = (10,5))
plt.title("EMS")
plt.tight_layout()


# #creating heatmaps of our data using seaborn
# Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an unstack method. Reference the solutions if you get stuck on this!**

# In[114]:


dayHour = df.groupby(by = ['Day of Week', 'Hour']).count()['reason'].unstack()


# In[118]:


plt.figure(figsize = (10,8))
sns.heatmap(dayHour, cmap = 'viridis')


# In[120]:


sns.clustermap(dayHour, cmap = 'viridis')


# In[122]:


dayMonth = df.groupby(by = ['Day of Week', 'Month']).count()['reason'].unstack()


# In[127]:


plt.figure(figsize = (10,5))
sns.heatmap(dayMonth, cmap = 'viridis')


# In[128]:


sns.clustermap(dayMonth, cmap = 'viridis')


# In[ ]:




