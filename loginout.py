#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#start
 
users = {}
status = ""
count=0
SpecialSym =['$', '@', '#', '%'] 
val=True
 
def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    
 
def newUser():
    val=True
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        if len(createPassw) < 6: 
            print('length should be at least 6') 
            val = False
          
        if len(createPassw) > 20: 
            print('length should be not be greater than 8') 
            val = False

        if not any(char.isdigit() for char in createPassw): 
            print('Password should have at least one numeral') 
            val = False

        if not any(char.isupper() for char in createPassw): 
            print('Password should have at least one uppercase letter') 
            val = False

        if not any(char.islower() for char in createPassw): 
            print('Password should have at least one lowercase letter') 
            val = False

        if not any(char in SpecialSym for char in createPassw): 
            print('Password should have at least one of the symbols $@#') 
            val = False
        if val: 
            users[createLogin]=createPassw
            print("\n User created")        
 
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()
def logout():
    answer=input("Do you want to logout now? y/n?")
    if answer.lower().startswith("y"):
          print("ok, carry on then")
            #game continue rhegi. call that game function
    elif answer.lower().startswith("n"):
          print("ok, goodbye")
          exit()


# In[ ]:




