#!/usr/bin/env python
# coding: utf-8

# In[4]:


#q1.
num=int(input("enter number of your choice:"))

if num>0:
    print("number is positive")
elif num==0:
    print("number is zero")
else:
    print("number is negative")


# In[6]:


#q2.
num=int(input("enter number of your choice:"))

if num%2==0:
    print("number is even")
else:
    print("number is odd")


# In[7]:


1900/4


# In[11]:


#q3.
year=int(input("enter year of your choice:"))

if year%4==0 and year%10 !=0:
    print("it is a leap year")
elif year%4 ==0 and year%10==0:
    if year%400==0:
        print("it is leap year")
    else:
        print("not leap year")
else:
    print("not leap year")


# In[20]:


#q4.
num=int(input("enter any number greater than 1 :"))

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")


# In[35]:


#q5.

for num in range(1,10001):
    if num>1:
        for j in range(2,num):
            
            if num%j==0:
                break
        else:
            print(num)
    
            


# In[ ]:




