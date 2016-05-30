
# coding: utf-8

# # Data Exploration

# # Project: Police killings

# Data: https://github.com/fivethirtyeight/data/tree/master/police-killings

# In[4]:

import pandas as pandas
police_killings = pandas.read_csv('police_killings.csv', encoding='iso8859_1')


# In[5]:

police_killings.head()


# In[7]:

police_killings.columns


# In[8]:

counts = police_killings['raceethnicity'].value_counts()


# In[9]:

print(counts)


# In[11]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import numpy as np

plt.bar(range(6), counts)
plt.xticks(range(6), counts.index, rotation="vertical")


# In[12]:

counts / sum(counts)


# ## Racial breakdown

# It looks like people identified as Black are far overrepresented in the shootings versus in the population of the US (28% vs 16%). You can see the breakdown of population by race here: https://en.wikipedia.org/wiki/Race_and_ethnicity_in_the_United_States#Racial_makeup_of_the_U.S._population
# 
# People identified as Hispanic appear to be killed about as often as random chance would account for (14% of the people killed as Hispanic, versus 17% of the overall population).
# Whites are underrepresented among shooting victims vs their population percentage, as are Asians.

# In[15]:

police_killings["p_income"][police_killings["p_income"] != "-"].astype(float).hist(bins=15)


# # Income breakdown

# According to the Census, median personal income in the US is 28,567, and our median is 22,348, which means that shootings tend to happen in less affluent areas. Our sample size is relatively small, though, so it's hard to make sweeping conclusions.

# In[17]:

state_pop = pandas.read_csv('state_population.csv')


# In[23]:

counts = police_killings["state_fp"].value_counts() 


# In[24]:

states = pandas.DataFrame({"STATE": counts.index, "shootings": counts })


# In[26]:

states = states.merge(state_pop, on="STATE")


# In[27]:

states["pop_millions"] = states["POPESTIMATE2015"] / 1000000
states["rate"] = states["shootings"] / states["pop_millions"]

states.sort("rate")


# ## Killings by state

# States in the midwest and south seem to have the highest police killing rates, whereas those in the northeast seem to have the lowest.

# In[28]:

police_killings["state"].value_counts()


# In[29]:

pk = police_killings[
    (police_killings["share_white"] != "-") & 
    (police_killings["share_black"] != "-") & 
    (police_killings["share_hispanic"] != "-")
]

pk["share_white"] = pk["share_white"].astype(float)
pk["share_black"] = pk["share_black"].astype(float)
pk["share_hispanic"] = pk["share_hispanic"].astype(float)


# In[30]:

lowest_states = ["CT", "PA", "IA", "NY", "MA", "NH", "ME", "IL", "OH", "WI"]
highest_states = ["OK", "AZ", "NE", "HI", "AK", "ID", "NM", "LA", "CO", "DE"]

ls = pk[pk["state"].isin(lowest_states)]
hs = pk[pk["state"].isin(highest_states)]


# In[31]:

columns = ["pop", "county_income", "share_white", "share_black", "share_hispanic"]

ls[columns].mean()


# In[32]:

hs[columns].mean()


# ## State by state rates

# It looks like the states with low rates of shootings tend to have a higher proportion of blacks in the population, and a lower proportion of hispanics in the census regions where the shootings occur. It looks like the income of the counties where the shootings occur is higher. States with high rates of shootings tend to have high hispanic population shares in the counties where shootings occur.
