#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import random as rn
import time


def question_number(l,n):
    j=rn.randint(0,n-1)
    if j in l:
        question_number(l,n) 
    else:
        l.append(j)
        return(int(j))


def help(h1,h2):
    print()
    print('Starcast:',h1)
    print('Release:',h2)


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


def play(q,h1,h2):
    tries=5
    out=['a','e','i','o','u','A','E','I','O','U','/','-']
    print()
    global h
    flg=0
    while tries>0:
        check=[]
        print()
        print(f'Tries:{tries}')
        print(f'Hints:{h}')
        print('Score:',score)
        print()
        ans=input('INPUT:')
        if ans in q:
            if ans not in out:
                out.append(ans)
        elif ans=='qt':
            exit()
        elif ans=='hm':
            pass #home function
        elif ans=='hp':
            if flg==0:
                if h>0:
                    hlp(h1,h2)
                    h-=1
                    flg+=1
                    continue
                else:
                    print('Help finished')
                    continue
            else:
                print('Help Already Used')
                continue
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


def show(q,h1,h2):
    vowels=['a','e','i','o','u','A','E','I','O','U','/','-']
    numb=[0,1,2,3,4,5,6,7,8,9]
    num_count=0
    print()
    for i in q:
        time.sleep(0.5)
        if i in numb:
            num_count+=1
        if i in vowels:
            print(f' {i}',end='')
        elif i==' ':
            print(' /',end='')
        else:
            print(' _',end='')
    print()
    if num_count!=0:
        print('It contains number [0-9]')
        print()
    play(q,h1,h2)
   
    
    
    


# In[ ]:


def game_play(n,film,star,dt):
    l=[]
    global score
    for i in range(10):
        print("Type 'hp' for hint")
        print("Type 'hm' to go home")
        print("Type 'qt' to quit")
        print()
        print(f'Quest.{i+1}')
        s=question_number(l,n)
        quest =film[s][0]    
        show(quest.lower(),star[s][0],dt[s][0])
        score+=10
        


# In[ ]:


def hollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-Easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    hollywood_medium()
    

        


# In[ ]:


def hollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    hollywood_hard()
    


# In[ ]:


def hollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Hollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Star Cast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    #game finishded
    


# In[ ]:


def bollywood_easy():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-easy.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    bollywood_medium()


# In[ ]:


def bollywood_medium():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\Bollywood-medium.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    bollywood_hard()


# In[ ]:


def bollywood_hard():
    df=pd.read_csv('C:\\Users\sudee\OneDrive\Desktop\bollywood-hard.csv')
    df.head()
    movie_name=np.asanyarray(df[['Name']])
    star_cast=np.asanyarray(df[['Starcast']])
    release=np.asanyarray(df[['Year']])
    n=len(movie_name)
    game_play(n,movie_name,star_cast,release)
    #game finished()


# In[ ]:


h=3
score=0


# In[ ]:


bollywood_easy()


# In[ ]:





# In[ ]:





# In[ ]:




