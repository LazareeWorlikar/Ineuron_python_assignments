#!/usr/bin/env python
# coding: utf-8

# In[22]:


#q1.
def fibonacci_series(n):
    if n>=2:
        return fibonacci_series(n-1)+fibonacci_series(n-2)
    else:
        return n
n=int(input("enter any positive integer:"))
for i in range(n):
    print(fibonacci_series(i))
    


# In[25]:


#q2.

def factorial(n):
    if n>0:
        return factorial(n-1)*n
    else:
        return 1


# In[27]:


factorial(4)


# In[29]:


#q3.

def bmi(weight,height):
    return (weight/(height**2))
weight=float(input("enter weight in kgs:"))
height=float(input("enter height in meters:"))

bmi(weight,height)


# In[31]:


#q4.
import math
num=float(input("enter any number:"))

print(f"the natural log of{num} is {math.log(num)}")


# In[45]:


#q5.
def cube(n):
    for i in range(1,n+1):
        print(i**3,end=", ")
         
   


# In[46]:


cube(3)


# In[ ]:




