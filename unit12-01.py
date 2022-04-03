#!/usr/bin/env python
# coding: utf-8

#12.지하철 시간대별 데이터 시각화하기

# In[1]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
for row in data :
    print(row)


# In[13]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
for row in data :
    row[4:] = map(int,row[4:])
    print(row)


# In[15]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
result=[]
for row in data :
    row[4:] = map(int,row[4:])
    result.append(row[10])
    print(len(result))
    print(result)


# In[16]:


import matplotlib.pyplot as plt
plt.bar(range(len(result)), result)
plt.show()


# In[17]:


import matplotlib.pyplot as plt
result.sort()  # 오름차순으로 정렬
plt.bar(range(len(result)), result)
plt.show()


# In[20]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = 0               # 최댓값을 저장할 변수 초기화
mx_station = ''     # 최댓값을 갖는 역 이름 저장 변수 초기화
for row in data :    # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx :
        mx = sum(row[10:15:2])
        mx_station = row[3]+'('+row[1]+')'
print(mx_station, mx)


# In[21]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = 0               # 최댓값을 저장할 변수 초기화
mx_station = ''     # 최댓값을 갖는 역 이름 저장 변수 초기화
for row in data :    # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
    row[4:] = map(int, row[4:])
    a = row[11:16:2]    #하차 인원 값 추출하기
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3]+'('+row[1]+')'
print(mx_station, mx)


# In[27]:


import csv
f = open('subwaytime.csv' , 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = 0   
mx_station = ''
t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? : '))
                                
for row in data :
    row[4:] = map(int, row[4:])
    a = row[4+(t-4)*2]          # 입력 받은 시각의 승차 인원 값 추출하기
    if a > mx :                 # 모든 데이터 탐색
        mx = a
        mx_station = row[3]+'('+ row[1]+')'
print(mx_station, mx)           # 승차 인원이 가장 큰 역과 인원 값 출력


# In[7]:


import csv
f = open('subwaytime.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = [0]*24
mx_station = ['']*24
for row in data :
    row[4:]=map(int,row[4:])
    for j in range(24) :
        a=row[j*2+4]
        if a>mx[j]:
                mx[j] = a
                mx_station[j] = row[3]+'(' + str(j+4) + '시)'
print(mx_station)
print(mx)


# In[9]:


import csv
import matplotlib.pyplot as plt
f = open('subwaytime.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = [0]*24 #시간대별 최대 승차 인원을 저장할 리스트 초기화
mx_station = ['']*24 #시간대별 최대 승차 인원 역 이름을 저장할 리스트 초기화
for row in data :
    row[4:]=map(int,row[4:])
    for j in range(24) :
        a=row[j*2+4] #j값과 인데스 번호 값의 관계식 사용
        if a>mx[j]:
                mx[j] = a
                mx_station[j] = row[3]+'(' + str(j+4) + '시)'
plt.rc('font',family='AppleGothic')
plt.bar(range(24),mx, color='b') # 막대그래프 속성 변경
plt.xticks(range(24),mx_station, rotation=90)
plt.show()


# In[10]:


import csv
import matplotlib.pyplot as plt
f = open('subwaytime.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)
mx = [0]*24 #시간대별 최대 하차 인원을 저장할 리스트 초기화
mx_station = ['']*24 #시간대별 최대 하차 인원 역 이름을 저장할 리스트 초기화
for row in data :
    row[4:]=map(int,row[4:])
    for j in range(24) :
        a=row[j*2+5] #j값과 인데스 번호 값의 관계식 사용
        if a>mx[j]:
                mx[j] = a
                mx_station[j] = row[3]+'(' + str(j+4) + '시)'
plt.rc('font',family='AppleGothic')
plt.bar(range(24),mx, color='b') # 막대그래프 속성 변경
plt.xticks(range(24),mx_station, rotation=90)
plt.show()


# In[15]:


import csv
import matplotlib.pyplot as plt 

f = open('subwaytime.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
next(data)

s_in = [0]*24 # 승차인원을 저장할 리스트 초기화
s_out = [0]*24 # 하차인원을 저장할 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for i in range(24) :
        s_in[i] += row[4+i*2] 
        s_out[i] += row[5+i*2]
        
        
plt.rc('font', family='AppleGothic')
plt.title('지하철 시간대별 승하차 인원 추이') # 제목 추가
plt.plot(s_in, label='승차') # 승차 인원을 꺾은 선 그래프로 표현
plt.plot(s_out, label='하차') # 하차 인원을 꺾은 선 그래프로 표현
plt.legend()
plt.xticks(range(24), range(4,28))
plt.show()


# In[ ]:




