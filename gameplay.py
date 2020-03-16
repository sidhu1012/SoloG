#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random as rn
import time


# In[2]:


def question_number(l,n):
    j=rn.randint(0,n-1)
    if j in l:
        question_number(l,n)  #error_maybe
    else:
        l.append(j)
    return(int(j))


# In[3]:


def play(tries):
    pass


# In[17]:


def show(q,tries):
    vowels=['a','e','i','o','u','A','E','I','O','U','/','-']
    for i in q:
        time.sleep(0.5)
        if i in vowels:
            print(f' {i}',end='')
        elif i==' ':
            print(' /',end='')
        else:
            print(' _',end='')
    print()
   # play() work in progress
                
    
    
    


# In[5]:


def game_play(tries,n,film):
    hints=3
    l=[]
    for i in range(10):
        print(f'Quest.{i+1}')
        s=question_number(l,n)
        quest =film[s][0]    # error
        show(quest,tries)
        


# In[14]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)
    

        


# In[7]:


def hollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)
    


# In[8]:


def hollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(5,n,movie_name)
    


# In[9]:


def bollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)


# In[10]:


def bollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)


# In[11]:


def bollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\bollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(5,n,movie_name)


# In[15]:


hollywood_easy()


# In[16]:


bollywood_easy()


# In[ ]:




