#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
print(data)
f.close()


# In[5]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
for row in data : 
    print(row)
f.close()


# In[6]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
f.close()


# In[7]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
header = next(data)
for row in data :
    print(row)
f.close()


# In[ ]:




