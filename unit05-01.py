#!/usr/bin/env python
# coding: utf-8

#5.내 생일의 기온 변화를 그래프로 그리기

# In[5]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
for row in data:
    print(row)


# In[6]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
for row in data:
    print(row[-1])


# In[7]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
result = []
for row in data:
    if row[-1] != '': # 최고 기온 데이터 값이 존재한다면 
        result.append(float(row[-1])) # result 리스트에 최고 기온 값 추가
print(result)
print(len(result))


# In[8]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
result = []
for row in data:
    if row[-1] != '': # 최고 기온 데이터 값이 존재한다면 
        result.append(float(row[-1]))# result 리스트에 최고 기온 값 추가
        
plt.plot(result, 'r')
plt.show()


# In[15]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
result = []
for row in data:
    if row[-1] != '': # 최고 기온 데이터 값이 존재한다면 
        result.append(float(row[-1]))# result 리스트에 최고 기온 값 추가
plt.figure(figsize = (12,4)) #가로로 12인치, 세로로 4인치 설정      
plt.plot(result, 'r')
plt.show()


# In[16]:


s='hello python'
print(s.split())


# In[17]:


data='2022-02-02'
print(data.split())


# In[18]:


data='2022-02-02'
print(data.split('-')[0])
print(data.split('-')[1])
print(data.split('-')[2])


# In[89]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
result = []
for row in data: 
    if row[-1] != '': #최고 기온값이 존재한다면
        if row[0].split('/')[0] == '8': #8월에 해당하는 값이라면
            result.append(float(row[-1])) #result 리스트에 최고 기온 값 추가
plt.figure(figsize = (12,4)) 
plt.plot(result, 'hotpink') #result 리스트에 저장된 값을 hotpink 색으로 그리기
plt.show()


# In[88]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
result = []
for row in data: 
    if row[-1] != '': #최고 기온값이 존재한다면
        if row[0].split('/')[0] == '8' and row[0].split('/')[1] == '14': #8월 14일에 해당하는 값이라면
            result.append(float(row[-1])) #result 리스트에 최고 기온 값 추가
plt.figure(figsize = (12,4)) 
plt.plot(result, 'hotpink') #result 리스트에 저장된 값을 hotpink 색으로 그리기
plt.show()


# In[92]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
high = []
low = []

for row in data: 
    if row[-1] != '' and row[-2] != '': #최고 기온값과 최저 기온 값이 존재한다면
        if 83 <= int(row[0].split('/')[2]): #1983년 이후 데이터라면
            if row[0].split('/')[0] == '8' and row[0].split('/')[1] == '14': #8월 14일 해당하는 값이라면
                high.append(float(row[-1])) #최고 기온 값을 high 리스트에 저장
                low.append(float(row[-2])) #최저 기온 값을 low 리스트에 저장
plt.figure(figsize = (12,4)) 
plt.plot(high, 'hotpink') #low 리스트에 저장된 값을 hotpink
plt.plot(low, 'skyblue') #low 리스트에 저장된 값을 skyblue
plt.show()


# In[99]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #최고 기온 데이터를 저장할 리스트 생성
high = []
low = []

for row in data: 
    if row[-1] != '' and row[-2] != '': #최고 기온값과 최저 기온 값이 존재한다면
        if 83 <= int(row[0].split('/')[2]): #1983년 이후 데이터라면
            if row[0].split('/')[0] == '8' and row[0].split('/')[1] == '14': #8월 14일 해당하는 값이라면
                high.append(float(row[-1])) #최고 기온 값을 high 리스트에 저장
                low.append(float(row[-2])) #최저 기온 값을 low 리스트에 저장

plt.rc('font', family='AppleGothic') #애플고딕을 기본 글꼴로 설정
plt.title('내 생일의 기온 변화 그래프') #제목설정 
plt.rcParams['axes.unicode_minus']=False #마이너스 기호 깨짐 방지 
plt.figure(figsize = (12,4)) 
plt.plot(high, 'hotpink') #low 리스트에 저장된 값을 hotpink
plt.plot(low, 'skyblue') #low 리스트에 저장된 값을 skyblue
plt.show()




