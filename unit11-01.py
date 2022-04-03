#!/usr/bin/env python
# coding: utf-8

#11. 대중교통 데이터 시각화하기

# In[6]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data :
    print(row)


# In[8]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)


# In[12]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 : #만약 row6 값이 0이 아니라면
        rate = row[4] / row[6]
        if rate > mx : #만약 rate 값이 mx 값보다 크다면
            mx = rate #mx 값을 rate 값으로 업데이트로
            print(row, round(rate,2)) #업데이트된 값 출력
            # round(rate,2)는 rate 값을 소수점 둘째 자리까지 반올림하는 명령


# In[15]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6])>100000: #유무임 승차 인원 합해서 100,000명 이상
        rate = row[4] / (row[4]+row[6])
        if rate > mx : 
            mx = rate 
            print(row, round(rate,2))


# In[17]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6])>100000: #유무임 승차 인원 합해서 100,000명 이상
        rate = row[4] / (row[4]+row[6])
        if rate > 0.94 : 
            mx = rate 
            print(row, round(rate,2))


# In[95]:


import csv
f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6])>100000: 
        rate = row[4] / (row[4]+row[6])
        if rate > mx : 
            mx = rate 
            mx_station = row[3]+ ' '+ row[1]
print(mx_station, round(mx*100,2))


# In[97]:


import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data)
label = ['유임 승차','유임하차','무임 승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family='AppleGothic')

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+''+row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+' '+row[1]+'.png') # 이미지 파일로 저장
    plt.show()


# In[91]:





# In[78]:





# In[ ]:




