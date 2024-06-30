#!/usr/bin/env python
# coding: utf-8

# In[25]:


import zipfile
import pandas as pd
import random
from datetime import timedelta


# In[26]:


zip_file_path = 'C:/Users/user/Downloads/archive (11).zip'
extract_path = 'project_management_data'


# In[27]:


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)


# In[28]:


excel_file_path = f'{extract_path}/project Management.xlsx'
df = pd.read_excel(excel_file_path)


# In[29]:


print(df.columns)


# In[30]:


def add_random_dates(entry_date):
    if pd.isnull(entry_date):
        return entry_date
    random_days = random.choice([7, 14, 21])  
    complete_date = pd.to_datetime(entry_date) + timedelta(days=random_days)
    return complete_date


# In[31]:


df['COmpleteDate'] = df.apply(
    lambda row: add_random_dates(row['EntryDate']) if pd.isnull(row['COmpleteDate']) else row['COmpleteDate'],
    axis=1)


# In[35]:


df_filtered = df[['Company', 'EntryDate', 'COmpleteDate', 'Task Owner ']]


# In[38]:


new_csv_file_path = 'project_management_with_random_dates.csv'
df_filtered.to_csv(new_csv_file_path, index=False)
print(f"Data with random dates saved to {new_csv_file_path}")


# In[ ]:




