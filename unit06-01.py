#!/usr/bin/env python
# coding: utf-8

#6.기온 데이터를 다양하게 시각화하기

# In[2]:


import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,7,8,10])
plt.show()


# In[4]:


import random
print(random.randint(1,6))


# In[5]:


import random
dice = []
for i in range(5):
        dice.append(random.randint(1,6))
print(dice)


# In[8]:


import matplotlib.pyplot as plt
dice=[]
for i in range(5):
    dice.append(random.randint(1,6))
plt.hist(dice, bins=6)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
dice=[]
for i in range(100):
    dice.append(random.randint(1,6))
plt.hist(dice, bins=6)
plt.show()


# In[10]:


import matplotlib.pyplot as plt
dice=[]
for i in range(100000):
    dice.append(random.randint(1,6))
plt.hist(dice, bins=6)
plt.show()


# In[12]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
result=[]

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))
plt.hist(result, bins=100, color='r') #히스토그램 
plt.show()


# In[17]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
aug=[] #8월 최고 기온 값을 저장할 aug 리스트 생성

for row in data:
    month = row[0].split('/')[0] #/로 구분 값 중 첫번째 값을 month에 저장
    if row[-1] != '':
        if month == '8':
            aug.append(float(row[-1]))
plt.hist(aug, bins=100, color='r') #히스토그램 
plt.show()


# In[21]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
aug=[] #8월 최고 기온 값을 저장할 aug 리스트 생성
jan = [] #1월의 최고 기온 값을 저장할 jan 리스트 생성

for row in data:
    month = row[0].split('/')[0] #/로 구분 값 중 첫번째 값을 month에 저장
    if row[-1] != '':
        if month == '8':
            aug.append(float(row[-1]))
        if month == '1':
            jan.append(float(row[-1]))
plt.hist(aug, bins=100, color='r', label='Aug') #히스토그램 
plt.hist(jan, bins=100, color='g', label='Jan')
plt.legend()
plt.show()


# In[22]:


import matplotlib.pyplot as plt
import random

result = []
for i in range(13):
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()


# In[23]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
result=[]

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))
plt.boxplot(result)
plt.show()


# In[24]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
aug=[]
jan=[]
for row in data:
    month = row[0].split('/')[0]
    if row[-1] != '':
        if month == '8':
            aug.append(float(row[-1]))
        if month == '1':
            jan.append(float(row[-1]))
plt.boxplot(aug)
plt.boxplot(jan)
plt.show()


# In[25]:


import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
aug=[]
jan=[]
for row in data:
    month = row[0].split('/')[0]
    if row[-1] != '':
        if month == '8':
            aug.append(float(row[-1]))
        if month == '1':
            jan.append(float(row[-1]))
plt.boxplot([aug,jan])
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import csv

f=open('seoul.csv')
data=csv.reader(f)
next(data)

#월별 데이터를 저장할 리스트 month 생성(12개)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[-1] != '':
        #월과 같은 번호의 인덱스에 월별 데이터 저장
        month[int(row[0].split('/')[0])-1].append(float(row[-1]))
        
plt.boxplot(month)
plt.show()


# In[32]:


import matplotlib.pyplot as plt
import csv

f=open('seoul.csv')
data=csv.reader(f)
next(data)

#일별 데이터를 저장할 리스트 day 생성
day = []
for i in range(31):
    day.append([]) # day 리스트 내 31개 리스트 생성

for row in data:
    if row[-1] != '':
        if row[0].split('/')[0] == '8':# 8월이라면
        #최고 기온값 저장
            day[int(row[0].split('/')[1])-1].append(float(row[-1]))
        
plt.style.use('ggplot') # 그래프 스타일 지정
plt.figure(figsize=(10,5), dpi=300) #그래프 크기 수정
plt.boxplot(day, showfliers=False) #아웃라이어 값 생략
plt.show()



