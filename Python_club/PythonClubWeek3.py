#!/usr/bin/env python
# coding: utf-8

# In[1]:


True


# In[2]:


3>2


# Boolean

# In[3]:


8>9


# In[4]:


8==9


# In[5]:


8<=8


# In[7]:


8!=8 # this means not equal to


# In[8]:


# This is useful for if statements.


# In[11]:


if 8>7: # this actually means if true: because the computer reads a true statement as true
    print("hello")


# In[17]:


if 8>9: # hello does not print because this statement is false
    print("hello")


# In[18]:


a = 8==8 # 8==8 is a true statement. 


# In[19]:


a


# In[28]:


if a is False: # must use capital F here otherwise it won't work
    print("hello")
else:
    print("bye")


# In[29]:


# Boolean operators: and or not


# In[31]:


True and True


# In[34]:


(8>7) and (4<5) # both these statements are true. Brackets are not necessary but it makes it cleaner. 


# In[36]:


(10<9) and (5<6)


# In[37]:


if not 7>8: # if not statement
    print("ok")


# In[38]:


if 9>8 and 5>4:
    print("true")


# In[48]:


mylist = [2, 3, 5, 6, 10, 55, 44, 77, 30, 23, 87, 3]
for item in mylist:
    print(number)


# In[50]:


print(mylist)


# In[57]:


if item in mylist: # have to break down the statement. If there is an item in mylist. If statement is...
    if item<6:
        print(item)
    print("its less than six")


# In[58]:


mylist[0] = 5


# In[59]:


mylist


# In[60]:


#A tupple uses brackets. A list uses square brackets. 


# In[62]:


# KG API


# In[66]:


open("RandomText.txt").readlines() 


# In[67]:


open("RandomText.txt").read() # read is a property of open


# In[68]:


# shift tab brings up the docstring


# In[70]:


# Make a query in the KG query builder: https://query.kg.ebrains.eu


# In[91]:


dataset = open("result.json", encoding="utf8")


# In[92]:


type(8)


# In[93]:


type("blue")


# In[94]:


# JSON is a python dictionary


# In[95]:


import json


# In[96]:


dataset =json.load(dataset)


# In[97]:


type(dataset) # now it is defined as a dictionary


# In[99]:


dataset.keys() # keys is a function of dictionaries. What are the keys in this json dictionary?


# In[101]:


#how to index into a dictionary? Dictionary has curly brackets


# In[102]:


{"name":"harry","age":27}


# In[109]:


dataset = dataset["data"] # this takes the data from the dataset and converts it to a list


# In[117]:


familynames = [] # create an empty list
for item in dataset: # these are dictionaries with context and family name
    fn = (item["familyName"])
    familynames.append(fn)


# In[161]:


print(familynames) # this has appended all the family names to a list. 


# In[192]:


for x in familynames:
    if x == 'Kleven':
        print("Kleven")

    
    


# In[ ]:





# In[ ]:




