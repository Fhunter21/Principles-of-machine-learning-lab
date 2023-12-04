#!/usr/bin/env python
# coding: utf-8

# In[1]:


#We are using MONGODB as database
#install pymongo
get_ipython().system('pip install pymongo')
#import and use
import pymongo
from pymongo import MongoClient


# In[6]:


client = MongoClient("localhost",27017)
#open database
db = client['employeeDB']
#open collection
col = db['employees']
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = col.insert_many(mylist)
#extract data from collection
x = col.find()
for i in x:
    print(i)


# In[ ]:




