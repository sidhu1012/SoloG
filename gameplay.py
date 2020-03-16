#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import random as rn


# In[ ]:


def question_number(l,n):
    j=rn.randint(0,n-1)
    if j in l:
        question_number(l,n)  #error_maybe
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
        if i in vowels:
            print(f' {i}',end='')
        elif i==' ':
            print('/',end='')
        else:
            print(' _',end='')
    print()
   # play() work in progress
                
    
    
    


# In[ ]:


def game_play(tries,n,film):
    hints=3
    l=[]
    for i in range(10):
        print(f'Quest.{i}')
        s=question_number(l,n)
        quest =film[s][0]    # error
        show(quest,tries)
        


# In[ ]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(3,n,movie_name)
    

        


# In[ ]:


def hollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(4,n,movie_name)
    


# In[ ]:


def hollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(5,n,movie_name)
    


# In[ ]:





# In[ ]:




