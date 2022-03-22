#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
name=input('궁금한 동네를 입력해봐요 : ')
for row in data:
    if name in row[1] :
        for i in range(4,105) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break
import matplotlib.pyplot as plt
plt.plot(m, label='M')
plt.plot(f, label='F')
plt.legend()
plt.show()


# In[5]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
result=[]
name=input('궁금한 동네를 입력해봐요 : ')
for row in data:
    if name in row[1] :
        for i in range(4,105) :
            result.append(int(row[i])-int(row[i+103]))
        break
import matplotlib.pyplot as plt
plt.bar(range(101), result)
plt.show()


# In[13]:


import csv
import math
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
size = []
name=input('궁금한 동네를 입력해봐요 : ')
for row in data:
    if name in row[1] :
        for i in range(4,105) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103]))) #sqrt
        break
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family='AppleGothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(m,f, s=size, c=range(101), alpha=0.5, cmap='jet')#컬러맵 적용
plt.colorbar()
plt.plot(range(max(m)),range(max(m)), 'g')#추세선 추가
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()


# In[ ]:




