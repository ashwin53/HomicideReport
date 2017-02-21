
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np

pd.options.display.max_columns = 20
#output_notebook()

#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.


# In[4]:

# Data Frame from homicide.csv

Homicide = pd.read_csv('D:\Classes\data programming\database.csv')
Homicide = Homicide.replace('Unknown', np.nan)
Homicide = Homicide[Homicide['Victim Age'] <= 100]
Homicide


# In[5]:

# Perpitrator Sex Total Data frame

Perpetrator_sex= Homicide.groupby('Perpetrator Sex').size().sort_values(ascending=False).to_frame('Total').reset_index()
Perpetrator_sex


# In[13]:


# Bar chart for the Perpitrator sexes

from bokeh.plotting import figure, output_notebook, show
from bokeh.charts import Bar, Histogram, Line, output_file, show
from bokeh.charts.attributes import cat, color
pd.options.display.max_columns = 20
output_notebook()

Per_sexes = Bar(Perpetrator_sex, 
                values='Total', 
                label=cat(columns='Perpetrator Sex', sort=False), 
                color=color(columns='Perpetrator Sex', palette=['Red'], sort=False), 
                legend=False,
                title='Perpetrator Sexes')


show(Per_sexes)


# In[15]:

# Data frame for the Victim Count  

Victim_Count= Homicide.groupby('Victim Count').size().sort_values(ascending=False).to_frame('Total').reset_index()
Victim_Count


# In[16]:

# Bar chart for Victim Count

Vic_Count = Bar(Victim_Count, 
                values='Total', 
                label=cat(columns='Victim Count', sort=False), 
                color=color(columns='Victim Count', palette=['Green'], sort=False), 
                legend=False,
                title='Victim_Counts')


show(Vic_Count)


# In[17]:

#Weapon Series used and it's total

Weapon_Series= Homicide.groupby('Weapon').size().sort_values(ascending=False).to_frame('Total').reset_index()
Weapon_Series


# In[18]:

#Bar Chart for Wepaon's used 

Weapon_Ser = Bar(Weapon_Series, 
                values='Total', 
                label=cat(columns='Weapon', sort=False), 
                color=color(columns='Weapon', palette=['Green'], sort=False), 
                legend=False,
                title='Weapon_Series')


show(Weapon_Ser)


# In[23]:

# Top Cities affeted by the homicide data frame

top_cities = Homicide.groupby('City').size().sort_values(ascending=False).to_frame('Total').reset_index().head(15)
top_cities


# In[24]:

# Bar Chart 

cities = Bar(top_cities,
             values='Total',
             label=cat(columns='City', sort=False),
             color=color(columns='City', palette=['Red'], sort=False),
             legend=False,
             title="Cities")

show(cities)


# In[28]:

# Dataframe for all the Races (Victim Race) and it's Total

df = pd.DataFrame()
df
df['Black'] = Homicide[(Homicide['Victim Race'] == 'Black')]['Year'].value_counts()
df['White'] = Homicide[(Homicide['Victim Race'] == 'White')]['Year'].value_counts()
df['Native'] = Homicide[(Homicide['Victim Race'] == 'Native American/Alaska Native')]['Year'].value_counts()
df['Asian'] = Homicide[(Homicide['Victim Race'] == 'Asian/Pacific Islander')]['Year'].value_counts()
df['Total'] = Homicide[Homicide['Victim Race'] != np.nan]['Year'].value_counts()

df = df.reset_index().rename(columns={'index': 'Year'})
df


# In[29]:

#bar chart for the Victim"s Race Yearwise and it's comparison

show(Bar(df,
          values=blend('Black', 'White', 'Asian', 'Native', name='victims', labels_name='victim'),
          label=cat(columns='Year', sort=True),
          stack=cat(columns='victim', sort=True),
          color=color(columns='victim', palette=['Red', 'Green', 'Blue','Yellow'], sort=False),
          legend='top_right',
          title="Victims per Race"))


# In[80]:

df = pd.DataFrame()
df
df['Black'] = Homicide[(Homicide['Victim Race'] == 'Black')]['Year'].value_counts()
df['White'] = Homicide[(Homicide['Victim Race'] == 'White')]['Year'].value_counts()
df['Native'] = Homicide[(Homicide['Victim Race'] == 'Native American/Alaska Native')]['Year'].value_counts()
df['Asian'] = Homicide[(Homicide['Victim Race'] == 'Asian/Pacific Islander')]['Year'].value_counts()

df = df.reset_index().rename(columns={'index': 'Year'})
df


# In[94]:

import matplotlib.pyplot as plt
import numpy as np
x = np.array([6921,7252,7770,7899,7610,8044,8454,8500,7448,7485,7414,7245,7438,7226,7076])
y = np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])
plt.plot(range(2000,2015), x, 'o--')
plt.xlabel('Blacks as Victims')
plt.ylabel('Years')
plt.plot(range(2000,2015),y)
plt.show()


# In[106]:

import matplotlib.pyplot as plt
import numpy as np
x = np.array([6921,7252,7770,7899,7610,8044,8454,8500,7448,7485,7414,7245,7438,7226,7076])
x1= np.array([249,299,291,324,272,306,326,281,217,282,244,263,273,241,232])
x2= np.array([116,99,129,116,130,124,120,100,113,119,116,107,99,103,111])
x3= np.array([7210,7691,7864,7956,8007,8130,8161,8169,7566,7791,7177,6955,6985,7226,6660])
y = np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])
plt.plot(range(2000,2015), x1, 'o--')
plt.plot(range(2000,2015), x, 'o--')
plt.plot(range(2000,2015), x2, 'o--')
plt.plot(range(2000,2015), x3, 'o--')
#legend(x='Blacks',x1='Asian',x2='Native',x3='White','top_right')
plt.legend(loc='upper right')
plt.xlabel('Victims')
plt.ylabel('Years')
plt.plot(range(2000,2015),y)
plt.show()


# In[ ]:



