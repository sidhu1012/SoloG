#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import random as rn
import time


# In[ ]:


def question_number(l,n):
    j=rn.randint(0,n-1)
    if j in l:
        question_number(l,n) 
    else:
        l.append(j)
    return(int(j))


# In[ ]:


def play_show(q,out,check):
    print()
    for i in q:
        if i in out:
            print(f' {i}',end='')
            check.append(i)
        elif i==' ':
            print(' /',end='')
            check.append(i)
        else:
            print(' _',end='')
    print()
    print()


# In[ ]:


def play(q):
    tries=5
    out=['a','e','i','o','u','A','E','I','O','U','/','-']
    print()

    while tries>0:
        check=[]
        print()
        print(f'Tries:{tries}')
        print(f'Hints:{h}')
        print('score',score)
        print()
        ans=input('INPUT:')
        if ans in q:
            if ans not in out:
                out.append(ans)
        elif ans=='qt':
            exit()
        elif ans=='hm':
            pass #home function
        else:
            tries-=1
        play_show(q,out,check)
        if check==list(q):
            break
        #compare strings to break loop
    if tries==0:
        print("Out of tries")
        print('You Loose')
        print('Total Score:',score)
        quit()
        #home function
        
        
        
            
            
        


# In[ ]:


def show(q):
    vowels=['a','e','i','o','u','A','E','I','O','U','/','-']
    print()
    for i in q:
        time.sleep(0.5)
        if i in vowels:
            print(f' {i}',end='')
        elif i==' ':
            print(' /',end='')
        else:
            print(' _',end='')
    print()
    play(q)
   
    
    
    


# In[ ]:


def game_play(n,film):
    l=[]
    for i in range(10):
        print("Type 'hp' for hint")
        print("Type 'hm' to go home")
        print("Type 'qt' to quit")
        print()
        print(f'Quest.{i+1}')
        s=question_number(l,n)
        quest =film[s][0]    
        show(quest.lower())
        score+=10
        


# In[ ]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    hollywood_medium()
    

        


# In[ ]:


def hollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    hollywood_hard()
    


# In[ ]:


def hollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    #game finishded
    


# In[ ]:


def bollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    bollywood_medium()


# In[ ]:


def bollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    bollywood_hard()


# In[ ]:


def bollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\bollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name)
    #game finished()


# In[ ]:


global h
global score
h=3
score=0


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




