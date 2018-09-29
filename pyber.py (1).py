
# coding: utf-8

# # Pyber Data Analysis (2016)
# 
# Based on the pyber data,the majority of drivers live in urban area considering the larger size of the population. Which logically result in a higher number of rides. However, it will be interesting to see if increasing the amount of drivers in Suburban areas will result in an increased number of rides. Rural cities have the least amount of drivers, therefore the least amount of rides.
# 

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[470]:


# Dependencies and Setup
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from scipy.stats import sem
import seaborn as sns
import os


# In[471]:


# File to Load
file_to_load = "ride_data.csv"
# Read the City and Ride Data
ride_data = pd.read_csv(file_to_load)


# In[472]:


ride_data = pd.read_csv(file_to_load)
ride_data.head()


# In[473]:


file_to_load2 = "Data/city_data.csv"
city_data = pd.read_csv(file_to_load2)


# In[514]:


city_data = pd.read_csv(file_to_load2)
city_data.head()
#drop one duplicate record with same city name, same ride_ids but different # of drivers
city_data = city_data.drop_duplicates('city', keep = 'first')


# In[515]:


# Display the data table for preview
merged_list = pd.merge(ride_data, city_data, how="left", on=["city", "city"])


# In[516]:


merged_list.head()


# # Bubble plot of ride sharing data

# In[517]:


#  count of rides per city
total_ride = merged_list.groupby(by='city')['ride_id'].count()
# average fare in each city
ave_fare_city = round(merged_list.groupby(by='city')['fare'].mean(),2)
# driver count for each city
driver_count = merged_list.drop_duplicates(subset='city', keep='first').set_index('city')['driver_count']*8
# color: based on the type for each city
type_list = merged_list.drop_duplicates(subset='city', keep='first').set_index('city')['type']


# In[540]:


# create dataframe to work with
bubbleData_df = pd.DataFrame({'x':total_ride,'y':ave_fare_city,'z':driver_count,'City Type':type_list})

# create color list
color_list = {'Suburban':'lightskyblue', 'Urban':'lightcoral', 'Rural':'gold'}

# create scatterplot

sns.set(style='whitegrid', context='notebook')
bubblePlot=sns.lmplot('x', 'y', data=bubbleData_df, hue='City Type', palette=color_list,                      fit_reg=False, size=7.5,                      legend=True,legend_out=True,                      scatter_kws={'s':driver_count, 'alpha':0.5, 'edgecolors':'black', 'linewidths':2})

plt.xlim(0,60)
plt.ylim(15,45)
plt.title("Pyber Ridesharing Data (2016)",{'fontname':'Arial','fontsize':16})
plt.xlabel("Total Number of Rides (Per City)",{'fontname':'Arial','fontsize':12})
plt.ylabel("Average Fare ($)",{'fontname':'Arial','fontsize':12})
plt.savefig("Ride.png", bbox_inches = 'tight')
plt.show()


# # Total Fares by City Type

# In[528]:


# create dataframe
fare_City_df = pd.DataFrame(merged_list.groupby(by='type')['fare'].sum())

# Calculate Type Percents and create labels

labels = ['Rural', 'Suburban', 'Urban']
wedge_sizes = [fare_City_df['fare'][0]/fare_City_df['fare'].sum(),               fare_City_df['fare'][1]/fare_City_df['fare'].sum(),               fare_City_df['fare'][2]/fare_City_df['fare'].sum()]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0)

# create and display pie chart
fig1, ax1 = plt.subplots()
ax1.pie(wedge_sizes, labels=labels, autopct='%1.2f%%', startangle=90,        colors=colors, explode=explode, shadow=True)
ax1.axis('off')
plt.title("Total Fares by City Type",{'fontname':'Arial','fontsize':14})
plt.savefig("Ride.png", bbox_inches = 'tight')
plt.show()


# # Total Rides by City Type

# In[527]:


# create dataframe
ride_City_df = pd.DataFrame(merged_list.groupby(by='type')['ride_id'].count())

# Calculate Type Percents and create labels

labels = ['Rural', 'Suburban', 'Urban']
wedge_sizes = [ride_City_df['ride_id'][0]/ride_City_df['ride_id'].sum(),               ride_City_df['ride_id'][1]/ride_City_df['ride_id'].sum(),               ride_City_df['ride_id'][2]/ride_City_df['ride_id'].sum()]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0)

# create and display pie chart
fig1, ax1 = plt.subplots()
ax1.pie(wedge_sizes, labels=labels, autopct='%1.2f%%', startangle=90,        colors=colors, explode=explode, shadow=True)
ax1.axis('off')
plt.title("Total Fares by City Type",{'fontname':'Arial','fontsize':14})
plt.savefig("Ride.png", bbox_inches = 'tight')
plt.show()


# # Total Drivers by City Type

# In[526]:


# create dataframe
drivers_City_df = pd.DataFrame(merged_list.groupby(by='type')['driver_count'].sum())

# create labels and calc
labels = ['Rural', 'Suburban', 'Urban']
wedge_sizes = [drivers_City_df['driver_count']['Rural']/drivers_City_df['driver_count'].sum(),               drivers_City_df['driver_count']['Suburban']/drivers_City_df['driver_count'].sum(),               drivers_City_df['driver_count']['Urban']/drivers_City_df['driver_count'].sum()]
explode = (0.1, 0.1, 0)

# create and display pie chart
fig1, ax1 = plt.subplots()
ax1.pie(wedge_sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=colors, explode=explode)
ax1.axis('off')
plt.title("Total Drivers by City Type",{'fontname':'Arial','fontsize':14})
plt.savefig("Ride.png", bbox_inches = 'tight')

plt.show()

