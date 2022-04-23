#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import choice

places = ['Mcdonalds', 'KFC', 'Burger King', 'Panda Express', 'Tutta Bella','Bok a Bok Fried Chicken','El Camion']

def pick(): 
    """Return Random Restaurant"""
    return choice(places)

