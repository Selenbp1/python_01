#2.서울의 기온 데이터 분석하기
#csv.reader() : CSV 파일에서 데이터를 읽어오는 함수
#csv.writer() : CSV 파일에 데이터를 저장하는 함수

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
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



