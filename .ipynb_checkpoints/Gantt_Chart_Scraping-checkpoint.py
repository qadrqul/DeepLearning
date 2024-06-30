#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install kaggle pandas')


# In[2]:


get_ipython().system('kaggle datasets download -d paultimothymooney/covid19-containment-and-mitigation-measures')


# In[6]:


import zipfile
import pandas as pd


# In[26]:


zip_file_path = 'C:/Users/user/Downloads/archive (8).zip'
extract_path = 'uber_data'


# In[27]:


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)


# In[28]:


uber_data_path = f'{extract_path}/My Uber Drives - 2016.csv'
uber_df = pd.read_csv(uber_data_path)


# In[29]:


uber_df.head()


# In[30]:


uber_filtered = uber_df[['START_DATE*', 'END_DATE*', 'CATEGORY*', 'MILES*']]


# In[31]:


uber_filtered.head()


# In[32]:


uber_filtered.to_csv('filtered_uber_data.csv', index=False)
print("Filtered Uber data saved to filtered_uber_data.csv")


# In[ ]:




