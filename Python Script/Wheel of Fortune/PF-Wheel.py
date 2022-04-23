#!/usr/bin/env python
# coding: utf-8

# In[11]:


answer=open ("WheelAnswer.txt")
for line in answer: 
    txt=line
    
missing_letters = len(txt)
while missing_letters != 0:
    print("Enter the guess")
    user_input = input()
    guess.append(user_input)
    print("-----")
    missing_letters = len(txt)
    for letter in txt:
        if letter in guess:
            missing_letters = missing_letters -1
            print(letter)
        else:
            print("?")

print("RAWR")


# In[ ]:





# In[ ]:




