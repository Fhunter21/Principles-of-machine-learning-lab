#!/usr/bin/env python
# coding: utf-8

# In[5]:


totalRecords=10
numberGolfRecreation=4
probGolf=numberGolfRecreation/totalRecords
print("Unconditio nal probability of golf: ={}".format(probGolf)) #conditional probability of `single' given`medRisk'
# bayes Formula #p(single|medRisk)=p(medRisk|single)p(single)/p(medRisk) #p(medRisk|single)=p(medRisk ∩single)/p(single)
# Therefore the result is:
numberMedRiskSingle=2 
numberMedRisk=3
probMedRiskSingle=numberMedRiskSingle/totalRecords
probMedRisk=numberMedRisk/totalRecords
conditionalProbability=(probMedRiskSingle/probMedRisk)
print("Conditional probability of single given medRisk: = {}".format(conditionalProbability))


# In[ ]:




