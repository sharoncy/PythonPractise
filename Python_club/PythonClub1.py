#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Morgan"
age = 6
food = "tuna"


# In[2]:


print(name, age, food)


# In[3]:


name + " is " + age + " years old and enjoys eating " + food


# In[4]:


name + " is " + str(age) + " years old and enjoys eating " + food


# In[10]:


def sentence_writer(name, age, food):
    output = name + " is " + str(age) + " years old and enjoys eating " + food
    print(output)
    


# Define a new function with arguments. Run the function with arguments.

# In[12]:


sentence_writer("Tom", 2, "apples")
sentence_writer("Rebecca", 3, "bananas")


# In[28]:


def sentence_writer(name, age, food):
    """This function writes a sentence about someone who enjoys eating food
    Parameters
    name: the name of the person eating food
    age: age of the person eating the food
    food: the food
    """
    output = name + " is " + str(age) + " years old and enjoys eating " + food
    return(output)


# In[19]:


Toms_food = sentence_writer("Tom", 2, "apples")
Rebeccas_food = sentence_writer("Rebecca", 3, "bananas")


# In[20]:


print(Toms_food)


# Return returns the value so it can be assigned to a new variable. 

# In[21]:


import MyLibrary


# In[22]:


MyLibrary sentence_writer2


# In[23]:


MyLibrary.sentence_writer2("George", 22, "potatoes")


# We created our own library and have used one of the functions in the library.

# In[24]:


import mylibrary as ml


# In[25]:


import MyLibrary as ml


# In[27]:


sentence_writer


# Use shift tab to see the documentation for the function. 

# In[30]:


sentence_writer(age = 16, food = "pumpkin", name = "possum")


# A library is a list of functions. Many developers create libraries with advanced functions.

# Conda comes preinstalled in anaconda

# In[34]:


import pandas as pd


# In[48]:


df = pd.read_csv("CustomRegions_All.csv",delimiter=";")
df


# In[44]:


region_names = df["Region name"]
region_pixels = df["Region pixels"]
object_pixels = df["Object pixels"]


# In[46]:


object_pixels/region_pixels


# In[49]:


normalised_objects = object_pixels/region_pixels


# In[50]:


normalised_objects.plot()


# In[ ]:




