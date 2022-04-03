#!/usr/bin/env python
# coding: utf-8

#9.우리 동네 인구 구조를 파이 차트로 나타내기

# In[4]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []
name=input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
    if name in row[1] :
        for i in row[4: 105] :
            m.append(-int(i))
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


# In[6]:


import matplotlib.pyplot as plt
plt.pie([10,20])
plt.show()


# In[7]:


import matplotlib.pyplot as plt
size = [2232,3323,1111,4123]
plt.axis('equal')
plt.pie(size)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
size = [2232,3323,1111,4123]
label = ['A', 'B', 'AB', 'O']
plt.axis('equal')
plt.pie(size, labels=label)
plt.show()


# In[10]:


import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
size = [2232,3323,1111,4123]
label = ['A', 'B', 'AB', 'O']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%')
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
size = [2232,3323,1111,4123]
label = ['A', 'B', 'AB', 'O']
color=['darkmagenta','deeppink', 'hotpink','pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', explode=(0,0,0.1,0))
plt.legend()
plt.show()


# In[22]:


import csv
f = open('gender.csv', 'r', encoding='utf8')
data = csv.reader(f)
size=[]
name=input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
    if name in row[1] :
        m=0
        f=0
        for i in range(101):
            m += int(row[i+4])
            f += int(row[i+107])
        break
size.append(m)
size.append(f)
import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
color=['darkmagenta','deeppink']
plt.axis('equal')
plt.pie(size, labels=['남','여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(name+'지역의 남녀 성별 비율')
plt.show()


