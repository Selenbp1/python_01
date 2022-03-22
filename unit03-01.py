#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()


# In[2]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
header = next(data)
for row in data:
    row[-1] = float(row[-1])#최고 기온을 실수로 변환
    print(row)
f.close()


# In[3]:


import csv
f = open('seoul.csv', 'r', encoding='utf8')
data = csv.reader(f)
header = next(data)
for row in data:
    if row[-1] =='':
        row[-1] = -999 #-999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    print(row)
f.close()


# In[13]:


import csv #CSV 모듈 불러오기
f = open('seoul.csv', 'r', encoding='utf8') #seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data) #맨 윗줄을 header 변수에 저장하기 
max_temp = -999 #최고 기온 값을 저장할 변수 초기화
max_date ='' #최고 기온이 가장 높았던 날짜를 저장할 변수 초기화
for row in data:
    if row[-1] =='': #만약 데이터가 누락되었다면 최고 기온을 -999로 저장
        row[-1] = -999 #-999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1]) #문자열로 저장된 최고 기온 값을 실수로 변환
    print(row)
    if max_temp < row[-1] : #만약 지금까지 최고 기온보다 더 높다면 업데이트
        max_date = row[0]
        max_temp = row[-1]
f.close()
print('기상관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로, ', max_temp,'도 였습니다.')


# In[ ]:





# In[ ]:




