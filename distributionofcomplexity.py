#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
from IPython.display import display, Markdown


# In[34]:


csv_file_path = 'project_management_with_random_dates.csv'
df = pd.read_csv(csv_file_path)


# In[35]:


df.rename(columns={'COmpleteDate': 'CompleteDate', 'Task Owner ': 'Task Owner'}, inplace=True)


# In[36]:


def parse_dates(date_series):
    return pd.to_datetime(date_series, errors='coerce')


# In[38]:


df['EntryDate'] = parse_dates(df['EntryDate'])
df['CompleteDate'] = parse_dates(df['CompleteDate'])
task_counts = df['Company'].value_counts()
task_durations = (df['CompleteDate'] - df['EntryDate']).dt.days
unique_task_owners = df['Task Owner'].nunique()


# In[39]:


statistics = {
    'Total Projects': df['Company'].nunique(),
    'Total Tasks': len(df),
    'Average Tasks per Project': task_counts.mean(),
    'Median Tasks per Project': task_counts.median(),
    'Average Task Duration (days)': task_durations.mean(),
    'Median Task Duration (days)': task_durations.median(),
    'Unique Task Owners': unique_task_owners
}


# In[40]:


statistics_df = pd.DataFrame(statistics, index=[0])


# In[42]:


display(statistics_df)

for key, value in statistics.items():
    print(f"{key}: {value}")


# In[43]:


def extract_gantt_data(df):
    extracted_data = df[['Company', 'EntryDate', 'CompleteDate', 'Task Owner']].copy()
    extracted_data.columns = ['Task', 'Start', 'End', 'Owner']
    extracted_data['Start'] = pd.to_datetime(extracted_data['Start'], errors='coerce')
    extracted_data['End'] = pd.to_datetime(extracted_data['End'], errors='coerce')
    return extracted_data

extracted_data = extract_gantt_data(df)


# In[44]:


def convert_to_mermaid_gantt(data):
    mermaid_gantt = '```mermaid\ngantt\n    dateFormat  YYYY-MM-DD\n'
    mermaid_gantt += '    title Project Schedule\n'
    for index, row in data.iterrows():
        if pd.notna(row['Start']) and pd.notna(row['End']):
            mermaid_gantt += f"    {row['Task']} : {row['Owner']}, {row['Start'].date()}, {row['End'].date()}\n"
    mermaid_gantt += '```'
    return mermaid_gantt

mermaid_gantt = convert_to_mermaid_gantt(extracted_data)
display(Markdown(mermaid_gantt))


# In[45]:


def generate_natural_language_instructions(data):
    instructions = "Project Schedule Instructions:\n"
    for index, row in data.iterrows():
        if pd.notna(row['Start']) and pd.notna(row['End']):
            instructions += f"Task '{row['Task']}' assigned to {row['Owner']} starts on {row['Start'].date()} and ends on {row['End'].date()}.\n"
    return instructions

instructions = generate_natural_language_instructions(extracted_data)
print(instructions)

