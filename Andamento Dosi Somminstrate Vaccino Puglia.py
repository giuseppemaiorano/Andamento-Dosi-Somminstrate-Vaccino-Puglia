#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


# In[7]:


df = pd.DataFrame({"Giorni" : [1, 2, 3, 4, 5, 6], 
                  "Dosi Somministrate" : [555, 1274, 179, 2903, 1921, 3539]})


# In[11]:



plt.plot(df["Giorni"], df["Dosi Somministrate"], linewidth=8)
plt.title("Andamento Dosi Somminstrate Vaccino Puglia")
plt.xlabel('Giorni')
plt.ylabel('Dosi Somministrate')


# In[ ]:




