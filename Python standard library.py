#!/usr/bin/env python
# coding: utf-8

# In[1]:


#max and min
l=max(1,5,66,2)
print(l)
#we can even pass the sequence to the max and min


# In[ ]:





# In[ ]:


#python standard library
#python provides several such useful values(constants),classes and functions.
#the collection of predefined utilies is refered as the python standard library.
#using this puthon standard library,
#->reusebility
#easy to mainatain


# In[5]:


#all these functions are organized into different modules
import math
import datetime
import collections


# In[ ]:


#math provides us to access some common math functions and constants


# In[6]:


math.factorial(5)


# In[7]:


math.pi


# In[8]:


import math as m1


# In[9]:


m1.pi


# In[12]:


from math import factorial,pi
factorial(5)


# In[ ]:


#let us discuss about random module
#randomness is useful in whenever uncertainity is required
#random module provides us utilities to create randomness


# In[24]:


#randint
#gives a random value between specified range,everytime you run it.
import random
l=random.randint(1,9)
print(l)


# In[ ]:


#choice
#it is a function in random module returns random value from the sequence


# In[26]:


l=random.choice([3,5,6,7,8])
print(l)


# In[ ]:


#we have different modules in python standard library


# In[ ]:


#letus dicuss about some more function
#map,reduce,filter
#map() applies  given function to each item of a sequence and returns a sequence of the results.
#map(fun,seq)


# In[28]:


def square(n):
    return n*n
l=[1,2,4,5]
r=map(square,l)
print(list(r))


# In[3]:


print("kabay")


# In[ ]:


l=input()
s_n=l.split()
m_o=map(int,s_n)
print(list(m_o))


# In[ ]:


#filter
#filter() method ,filters the elements of the given sequence based on the result of given function
#the function should return True/false


# In[11]:


#reduce is not a built in function
from functools import reduce


# In[10]:


len("bootle")

