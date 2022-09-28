#!/usr/bin/env python
# coding: utf-8

# Python club week 2. A list is a method for storing multiple values in a single variable. 

# In[74]:


mylist = ["A","B","C"]


# In[75]:


print(mylist)


# In[76]:


mylist[0]


# To get last element use -1, second last element is -2

# In[77]:


mylist[-1]


# In[78]:


myfruits = ["pineapple", 
            "apple", 
            "passionfruit", "mangoes"]


# In[79]:


for fruit in myfruits:
    print(fruit)


# In[80]:


for i in myfruits:
    print(i)
    print("-------")
print("finished")


# A for loop will run once for every item in the list. The indentation defines what belongs to the for loop. Lists have built in methods such as append, extend, etc. Different data types have different methods. 

# In[81]:


myfruits


# In[82]:


myfruits.append("orange")


# In[83]:


print(myfruits)


# In[84]:


set(myfruits)


# A set is a datatype that doesn't allow duplicates. 

# In[85]:


len(myfruits)


# In[86]:


mylist


# In[87]:


myfruits


# In[88]:


myfruits.extend(mylist)


# In[89]:


print(myfruits)


# In[90]:


biglist = []


# In[91]:


biglist.append(myfruits)


# In[92]:


print(biglist)


# In[93]:


biglist.extend(myfruits)


# In[94]:


print(biglist)


# Dictionaries uses curly braces. A JSON file is a dictionary. Define key:value pairs. Dictionaries are not indexed with numbers. They are indexed with keys. 

# In[95]:


mydictionary = {"a":1, "b":2, "c":3}


# In[96]:


mydictionary["b"]


# In[97]:


mydictionary.keys()


# In[98]:


list(mydictionary.keys())


# In[99]:


list(mydictionary.values())


# .values is a function. The arguments in a function are defined by (). keys() - this is a function that gives you everything. To use pd.DataFrame need lists. Libraries are collections of functions. 

# In[100]:


mydictionary = {"tracing_data":["Ulrike","Martin"],
                "dopamine_data":["Ingvild","Harry"],
                "alzheimer's data":["Maja","Sharon"],
                "thionine_data":["Camilla","Ingrid"]}


# In[101]:


mydictionary["dopamine_data"]


# In[102]:


import pandas as pd # pandas used for data science: work with dataframes.
import numpy as np # used to manipulate arrays

# apply the DataFrame function from the pd library to the mydictionary object
pd.DataFrame(mydictionary)


# Docstring = hover over the function and press shift tab. (fn lock and tab) 

# Docstring = shift tab. (fn lock and tab) 

# In[104]:


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rat = [12,34,45,41,76,74,33,33,22,53,22,12]


# In[109]:

# create an array
np.arange(start=0, stop=12) # a range (not arrange)


# In[116]:


mouse = np.random.randint(low=12,high=80,size=12) # generate a random list between 12 and 80 with 12 values. 
# This generates an array. An array can be 2 or 3 dimensional. 


# In[113]:


print(mouse)


# In[114]:


print(months)
print(rat)
print(mouse)


# In[120]:

# matplotlib.pyplot is the plotting library
import matplotlib.pyplot as plt


# In[119]:


#There are two ways for generating plots with matplotlib. One is quick and easy. They other makes professional plots. 
#First we will look at the simple way.


# In[141]:

# use the plot function to plot months versus rat
plt.plot(months,rat,label ="rat", color ="red") # plot is a line plot.
plt.plot(months,mouse,label = "mouse")
plt.legend()
plt.xlabel("Month")
plt.ylabel("#no of datasets")
plt.show() # display the plot. 


# In[140]:


#The more advanced plotting option gives more options. It also uses matplotlib.pyplot. The benefit of this figure interface is that we can adjust the figure size. 


# In[154]:


fig, ax = plt.subplots(figsize=(10,4)) # define the proportions of the plot. 
ax.plot(months,rat, label="rat", color="red")
ax.plot(months,mouse, label="mouse",color="blue")
ax.set_xlabel("month")
ax.set_ylabel("# of datasets")
plt.savefig("myplot.svg") # this produces a scalable vector. 
plt.show()


# In[156]:


fig, ax = plt.subplots(figsize=(10,4)) # define the proportions of the plot. 
ax.bar(months,rat, label="rat", color="red")
ax.bar(months,mouse, label="mouse",color="blue", bottom=rat)
ax.set_xlabel("month")
ax.set_ylabel("# of datasets")
plt.savefig("myplot.svg") # this produces a scalable vector. 
plt.show()


# In[157]:


fig, ax = plt.subplots(figsize=(10,4)) # define the proportions of the plot. 
ax.scatter(months,rat, label="rat", color="red")
ax.scatter(months,mouse, label="mouse",color="blue")
ax.set_xlabel("month")
ax.set_ylabel("# of datasets")
plt.savefig("myplot.svg") # this produces a scalable vector. 
plt.show()


# In[3]:


get_ipython().system('jupyter nbconvert --to python ')


# In[ ]:





# In[ ]:




