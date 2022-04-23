#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pandasql')


# In[3]:


import pandas as pd
import pandasql as psql
#import os
#os.getcwd()


# ## Read the data sources from csv and store them in pandas dataframes

# In[9]:





# In[24]:


#read and store director and movie data
movie_director = pd.read_csv('disney_files/disney-director.csv')
#read and store movie income data
movie_income = pd.read_csv('disney_files/disney_movies_total_gross.csv')
#read and store annual revenue data      
yearly_revenue = pd.read_csv('disney_files/disney_revenue_1991-2016.csv')
#read and store disney characters
disney_characters = pd.read_csv('disney_files/disney-characters.csv')


# In[21]:


#show sample movie_director data
movie_director.head()


# In[14]:


#show sample movie_director data
movie_income.head()


# In[30]:


#get data types of columns
movie_income.dtypes


# In[22]:


#show yearly revenue data
yearly_revenue.head()


# In[25]:


#show disney characters
disney_characters.head()


# # Q1: Store revenue and count of movies by director
# 

# In[32]:


movie_income['total_gross'] =  movie_income['total_gross'].str.replace('$', '')
movie_income['total_gross'] =  movie_income['total_gross'].str.replace(',', '')
movie_income['total_gross'] = movie_income['total_gross'].astype(int)


# In[33]:


query = """select md.director, count(md.name) as no_of_movies,  sum(mi.total_gross) as total_revenue
from movie_director as md 
join movie_income as mi on md.name = mi.movie_title group by md.director """


# In[36]:


director_revenue = psql.sqldf(query)


# In[37]:


director_revenue.head()


# # Q2: What movies were made from 1991 to 1999, and what was their total gross income
# 

# In[52]:


#Using Pandas filters
movie_income.head()
movie_income['release_date'] = pd.to_datetime(movie_income['release_date'])


# In[54]:


movie_income.head()


# In[59]:


filtered_movies = movie_income[((movie_income.release_date >= '1991-01-01') & (movie_income.release_date <= '1999-12-31'))]


# In[60]:


filtered_movies.head()


# In[70]:


#total income from movies released between 1991 and 1999
try:
    
    income_91_to_99 = filtered_movies.total_gross.sum()
    print("Total Income between 1991 and 1999 is: " + str(income_91_to_99))

except: 
    print ("Invalid Calculation")


# # Q3: What movie genre did each villian appear in? 

# In[63]:


disney_characters['movie_title'] =  disney_characters['movie_title'].str.replace('\n', '')


# In[64]:


disney_characters.head()


# In[65]:


#disney_character & movie_income

villian_genre = movie_income.merge(disney_characters, how='inner', on='movie_title')


# In[66]:


villian_genre.head()


# In[67]:


villian_genre = villian_genre [["movie_title", "villian", "genre"]]


# In[68]:


villian_genre.head()


# In[ ]:




