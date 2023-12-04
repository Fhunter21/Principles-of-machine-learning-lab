#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[4]:


data=fetch_20newsgroups() #fetching new group data
text_categories=data.target_names #storing the target variable
#splitting the data
train_data=fetch_20newsgroups(subset="train",categories=text_categories)
test_data=fetch_20newsgroups(subset="test",categories=text_categories)
#vectorizing data
model=make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(train_data.data,train_data.target)
predicted_categories=model.predict(test_data.data)
mat=confusion_matrix(test_data.target,predicted_categories)
sns.heatmap(mat.T,square=True,annot=True,fmt="d",xticklabels=train_data.target_names,yticklabels=train_data.target_names)
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()
print("The accuracy is {}".format(accuracy_score(test_data.target,predicted_categories)))


# In[ ]:




