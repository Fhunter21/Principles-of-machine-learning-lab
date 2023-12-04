#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 
from sklearn.datasets import load_breast_cancer 
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
import seaborn as sns 
sns.set()


# In[3]:


breast_cancer = load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
print(X)
X = X[['mean area', 'mean compactness']]
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y = pd.get_dummies(y, drop_first=True)
#Train test split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[5]:


knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean') 
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# In[6]:


sns.scatterplot( x='mean area', y='mean compactness', hue='benign', data=X_test.join(y_test, how='outer') )


# In[7]:


confusion_matrix(y_test, y_pred)


# In[9]:


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

