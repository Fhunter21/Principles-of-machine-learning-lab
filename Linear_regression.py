#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[17]:


data=pd.read_csv("C:/Users/saile/Desktop/Salary_Data.csv")


# In[18]:


data.head()


# In[19]:


data.isnull().sum


# In[20]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[21]:


X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values
print(X)
print(y)


# In[22]:


X_train,X_test,Y_train,Y_test=train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[23]:


regressor = LinearRegression()
regressor.fit(X_train, Y_train)
print(" Accuracy=",regressor.score(X_test, Y_test))


# In[31]:


#Intercept and Coefficient
print("Intercept: ", regressor.intercept_)
print("Coefficient: ", regressor.coef_)
#Prediction of test set
y_pred_slr= regressor.predict(X_test)
#Predicted values
print("Prediction for test set: {}".format(y_pred_slr))


# In[33]:


#Actual value and the predicted value
regressor_diff = pd.DataFrame({'Actual value': Y_test, 'Predicted value': y_pred_slr})
regressor_diff.head()


# In[35]:


#Line of best fit
import matplotlib.pyplot as plt
plt.scatter(X_test,Y_test)
plt.plot(X_test,y_pred_slr, 'Red')
plt.show()


# In[ ]:




