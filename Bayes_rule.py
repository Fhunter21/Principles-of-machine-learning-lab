#!/usr/bin/env python
# coding: utf-8

# Week 1:  Aim : The probability that it is Friday and that a student is absent is 3 %. Since there are 5 school days in a week, the probability that it is Friday is 20 %. What is the probability that a student is absent given that today is Friday? Apply Baye’s rule in python to get the result.
# 
# 
# =================================
# Explanation:
# =================================
# 	F : Friday
# 	A : Absent
# 
# 	Based on the given problem statement,
# 
# 	The probability that it is Friday and that a student is absent is 3%
# 	i.e
# 	P(A ∩ F)= 3% = 3 / 100 = 0.03 
# 
# 	and
# 
# 	The probability that it is Friday is 20%
# 	i.e
# 
# 	P(F)=20% = 20/100 = 0.2 
# 
# 	Then,
# 
# 	The probability that a student is absent given that today is Friday
# 	P(A ∣ F)
# 
# 	By the definition of Baye's rule( conditional probability ), we have
# 
# 	P(A ∣ F) = P(A ∩ F) / P(F) 
# 

# In[11]:


pAF=0.03
print("The probability that it is Friday and that a student is absent :",pAF)
# The probability that it is Friday is 20%
pF=0.2
print("The probability that it is Friday : ",pF)
# The probability that a student is absent given that today is Friday
pResult=(pAF/pF)
# Display the Result
print("The probability that a student is absent given that today is Friday : ",pResult * 100,"%")

