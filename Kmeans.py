#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
X = np.array([[1.713,1.586], [0.180,1.786], [0.353,1.240], [0.940,1.566], [1.486,0.759], [1.266,1.106],[1.540,0.419],[0.459,1.799],[0.773,0.186]])
y=np.array([0,1,1,0,1,0,1,1,1])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X,y)
p=kmeans.predict([[0.906, 0.606]])
print('Prediction of classification for a case where VAR1=0.906 and VAR2=0.606,')
print('Class',p)


# In[ ]:




