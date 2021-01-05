#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


df = pd.DataFrame({"Giorni" : [1, 2, 3, 4, 5, 6], 
                  "Dosi Somministrate" : [555, 1274, 179, 2903, 1921, 3539]})


# In[20]:



plt.plot(df["Giorni"], df["Dosi Somministrate"], linewidth=8)
plt.title("Andamento Dosi Somministrate Vaccino Puglia")
plt.xlabel('Giorni')
plt.ylabel('Dosi Somministrate')


# In[21]:


for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)


# In[22]:


df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()


# In[23]:


df.head()


# In[30]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Dosi Somministrate'],label='Dosi Somministrate', linewidth=6)
plt.plot(df['SMA_3'],label='Media Mobile 3 giorni', linewidth=6)
plt.xlabel('Giorni')
plt.ylabel('Dosi Somministrate')
plt.title("Andamento Dosi Somministrate Vaccino Puglia", fontsize=20)
plt.legend(loc=2)


# In[ ]:




