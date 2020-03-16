#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import random as rn


# In[29]:


def question_number(l,n):
    j=rn.randint(0,n-1)
    if j in l:
        question(l)  #question not defined
    else:
        l.append(j)
    return(int(j))


# In[30]:


def play(tries):
    pass


# In[31]:


def show(q,tries):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in q:
        if tries==0:
            break #question screen function
        else:
            if i not in q:
                pass
                
    
    
    


# In[32]:


def game_play(tries,n,film):
    hints=3
    l=[]
    for i in range(10):
        print(f'Quest.{i}')
        s=question_number(l,n)
        quest =list(film[s])
        show(quest,tries)
        


# In[33]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(3,n,movie_name)
    

        


# In[34]:


def hollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)
    


# In[35]:


def hollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(5,n,movie_name)
    


# In[36]:


hollywood_easy()


# In[ ]:




