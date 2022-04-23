#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

villains = [
['Doctor', 'No'],
['Rosa', 'Klebb'],
['Mister', 'Big'],
['Auric', 'Goldfinger'],
['Ernst', 'Blofeld'],
]

with open('villains.csv', 'w', newline='') as file: 
    csvout = csv.writer(file)
    csvout.writerows(villains)

file.close()


# In[2]:


try:
    with open('villains.csv', 'r') as fin: 
        cin = csv.reader(fin)
        villains = [row for row in cin]
    
    print(villains)
except IndentationError: 
    print("Indentation Error Detected")
except FileNotFoundError:
    print("CSV file not found, please create")


# In[3]:


with open('villians.csv', mode='a', newline='') as f_object:
    csvout = csv.writer(f_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csvout.writerow(["Lucifer", "Morningstar"])
    
f_object.close()


# In[117]:


with open('villains.csv', 'r') as fin: 
    cin = csv.reader(fin)
    villains = [row for row in cin]
    
    print(villains)


# In[ ]:





# In[ ]:




