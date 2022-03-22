#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
plt.bar([0,1,2,4,6,10], [1,2,3,4,5,6])
plt.show()


# In[3]:


import matplotlib.pyplot as plt
plt.bar(range(6), [1,2,3,4,5,6])
plt.show()


# In[31]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

result=[]
for row in data:
        if '신도림' in row[1] :
            for i in row[3:]:
                result.append(int(i))
                
import matplotlib.pyplot as plt 
plt.bar(range(101), result)
plt.show()


# In[36]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

result=[]
for row in data:
        if '신도림' in row[1] :
            for i in row[3:]:
                result.append(int(i))
                
import matplotlib.pyplot as plt 
plt.barh(range(101), result)
plt.show()


# In[70]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
for row in data:
    if '신도림' in row[1] :
        for i in range(0,101) :
            m.append(int(row[i+4]))
            f.append(int(row[-(i+1)]))
f.reverse()


# In[68]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
for row in data:
    if '신도림' in row[1] :
        for i in row[4: 105] :
            m.append(int(i))
        for i in row[107:]:
            f.append(int(i))
import matplotlib.pyplot as plt
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()


# In[85]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
name=input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
    if name in row[1] :
        for i in row[4: 105] :
            m.append(int(i))
        for i in row[107:]:
            f.append(int(i))
        break
import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus']=False
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()


# In[ ]:




