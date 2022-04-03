#!/usr/bin/env python
# coding: utf-8

#7.우리 동네 인구 구조 시각화하기

# In[15]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data:
    print(row)


# In[16]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data:
    if '서울특별시 구로구 신도림동' == row[1]:
        print(row)


# In[17]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data:
    if '신도림' in row[1]:
        print(row)


# In[19]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data:
    if '신도림' in row[1]:
        for i in row[3:]:
            print(i)


# In[20]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for row in data:
    if '신도림' in row[1]:
        print(len(row[3:]))


# In[31]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []

for row in data:
    if '신도림' in row[1]: # 신도림이 포함된 행정구역 찾기
        for i in row[4:]: #0세부터 끝까지 모든 연령에 대해 반복
            result.append(i) #해당 연령의 인구수 리스트에 순서대로 저장
print(result) #0세부터 100세 이상까지의 인구수 출력


# In[42]:


import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []

for row in data:
    if '신도림' in row[1]: # 신도림이 포함된 행정구역 찾기
        for i in row[4:]: #0세부터 끝까지 모든 연령에 대해 반복
            result.append(int(i)) #해당 연령의 인구수 리스트에 순서대로 저장
print(result) #0세부터 100세 이상까지의 인구수 출력


# In[41]:


import matplotlib.pyplot as plt
import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []

for row in data:
    if '신도림' in row[1]: # 신도림이 포함된 행정구역 찾기
        for i in row[4:]: #0세부터 끝까지 모든 연령에 대해 반복
            result.append(i) #해당 연령의 인구수 리스트에 순서대로 저장
plt.style.use('ggplot') #격자무늬스타일 지정
plt.plot(result)
plt.show()


# In[40]:


import matplotlib.pyplot as plt
import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data:
    if '아름동' in row[1]: # 신도림이 포함된 행정구역 찾기
        for i in row[4:]: #0세부터 끝까지 모든 연령에 대해 반복
            result.append(int(i)) #해당 연령의 인구수 리스트에 순서대로 저장

plt.style.use('ggplot') #격자무늬스타일 지정
plt.rc('font', family='AppleGothic')
plt.title(name + '지역의 인구 구조')
plt.plot(result)
plt.show()

