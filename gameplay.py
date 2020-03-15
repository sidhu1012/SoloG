#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random as rn


# In[4]:


def question_number(l):
    j=rn.randint(50)
    if j in l:
        question(l)
    else:
        l.append(j)
    return(int(j))


# In[ ]:


def play(tries):
    pass


# In[ ]:


def show(q,tries):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in q:
        if tries==0:
            break #question screen function
        else:
            if i not in q:
                pass
                
    
    
    


# In[6]:


def game_play(tries):
    hints=3
    l=[]
    for i in range(10):
        print(f'Quest.{i}')
        s=question_number(l)
        quest =list(movie_name[s])
        show(quest,tries)
        


# In[5]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    game_play(3)
    

        


# In[ ]:





# In[ ]:




