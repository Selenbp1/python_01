#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 14.numpy를 활용한 나만의 프로젝트 만들기


# In[2]:


#전국에서 영유아들이 가장 많이 사는 지역은 어디일까?
#보통 학군이 좋다고 알려진 지역에는 청소년들이 많이 살까?
#광역시 데이터를 10년 단위로 살펴보면 청년 비율이 줄고 있다는 사실을 알 수 있을까?
#서울에서 지난 5년간 인구가 가장 많이 증가한 구는 어디일까?
#우리 동네의 인구 구조와 가장 비슷한 동네는 어디일까?


# In[3]:


#전국에서 신도림동의 연령별 인구 구조와 가장 형태가 비슷한 지역은 어디일까?
#1.데이터를 읽어온다.
#2.궁금한 지역의 이름을 입력받는다.
#3.궁금한 지역의 인구 구조를 저장한다.
#4.궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
#5.가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다.


# In[4]:


#1.데이터를 읽어온다.
import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
for row in data :
    print(row)


# In[5]:


#1.데이터를 읽어온다.
import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #데이터 처리에 불필요한 헤더 부분 제외
for row in data :
    print(row)


# In[12]:


#2.궁금한 지역의 이름을 입력받는다.
#3.궁금한 지역의 인구 구조를 저장한다.
import csv
f = open('age.csv', 'r', encoding='utf8')
data = csv.reader(f)
next(data) #데이터 처리에 불필요한 헤더 부분 제외
home=[] #입력받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[1]: #입력받은 지역의 이름이 포함된 행 찾기
        for i in row[4:] : #4번 인덱스 값부터 슬라이싱
            home.append(int(i)) #입력받은 지역의 데이터를 home에 저장
print(home) #home에 저장된 데이터 출력


# In[16]:


import numpy as np
import csv
f=open('age.csv', 'r', encoding='utf8')
data=csv.reader(f)
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[1]:
        home=np.array(row[4:], dtype=int)
print(home)


# In[18]:


import numpy as np
import matplotlib.pyplot as plt
import csv
f=open('age.csv', 'r', encoding='utf8')
data=csv.reader(f)
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[1]:
        home=np.array(row[4:], dtype=int)
plt.rc('font', family='AppleGothic')
plt.title(name+' 지역의 인구 구조')
plt.plot(home)
plt.show()


# In[22]:


#4.궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    #1)전국의 모든 지역 중 한 곳(B)을 선택한다.
    #2)궁금한 지역 A의 0세 인구수에서 B의 0세 인구수를 뺀다.
    #3) 2)를 100세 이상 인구수에 해당하는 값까지 반복한 후 각각의 차이를 모두 더한다.
    #4)전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.
import numpy as np
import matplotlib.pyplot as plt
import csv
f=open('age.csv', 'r', encoding='utf8')
data=csv.reader(f)
next(data)
data=list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[1]:
        home=np.array(row[4:], dtype=int)/int(row[3])#사용자로부터 입력받은 지역의 연령대별 인구 비율을 home에 저장하는 코드
for row in data:
    away=np.array(row[4:], dtype=int)/int(row[3])#다른 동네의 인구 비율을 away에 저장하는 것
    print(home - away) #home에 저장된 인구 비율과 away에 저장된 값의 차를 출력
plt.rc('font', family='AppleGothic')
plt.title(name+' 지역의 인구 구조')
plt.plot(home)
plt.show()  


# In[23]:


#4.궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    #1)전국의 모든 지역 중 한 곳(B)을 선택한다.
    #2)궁금한 지역 A의 0세 인구수에서 B의 0세 인구수를 뺀다.
    #3) 2)를 100세 이상 인구수에 해당하는 값까지 반복한 후 각각의 차이를 모두 더한다.
    #4)전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.
import numpy as np
import matplotlib.pyplot as plt
import csv
f=open('age.csv', 'r', encoding='utf8')
data=csv.reader(f)
next(data)
data=list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[1]:
        home=np.array(row[4:], dtype=int)/int(row[3])#사용자로부터 입력받은 지역의 연령대별 인구 비율을 home에 저장하는 코드
for row in data:
    away=np.array(row[4:], dtype=int)/int(row[3])#다른 동네의 인구 비율을 away에 저장하는 것
    print(np.sum(home - away)) #home에 저장된 인구 비율과 away에 저장된 값의 차를 출력
plt.rc('font', family='AppleGothic')
plt.title(name+' 지역의 인구 구조')
plt.plot(home)
plt.show()  


# In[31]:


#전국에서 신도림동의 연령별 인구 구조와 가장 형태가 비슷한 지역은 어디일까?

#1.데이터를 읽어온다.
import numpy as np
import matplotlib.pyplot as plt
import csv
f=open('age.csv', 'r', encoding='utf8')
data=csv.reader(f)
next(data)
data=list(data)

#2.궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn=1 #최솟값을 저장할 변수 생성 및 초기화
result_name='' #최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result=0 #최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화

#3.궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[1]:
        home=np.array(row[4:], dtype=int)/int(row[3])#사용자로부터 입력받은 지역의 연령대별 인구 비율을 home에 저장하는 코드

#4.궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data:
    away=np.array(row[4:], dtype=int)/int(row[3])#다른 동네의 인구 비율을 away에 저장하는 것
    s=np.sum((home-away)**2) #home에 저장된 값과 away에 저장된 값의 차이의 합을 계산
    if s < mn and name not in row[1] : #if 조건문 안에서는 위에서 계산한 합이 최솟값인지 확인
        #not in 연산을 사용하여, 입력받은 이름과 같은 이름이 아닌 데이터 중에서 최솟값을 찾
        #전국에서 인구 구조가 완전히 똑같은 지역은 없을 것이라고 가정하면 if 0 < s < mn : 와 같이 코드를 작성할 수도 있음
        mn = s #만약 최솟값이라면 변수 mn의 값을 갱신
        result_name=row[0]
        result=away

#5.가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다.
plt.rc('font', family='AppleGothic')
plt.title(name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name) #home 값을 그리는 그래프 레이블 설정
plt.plot(result, label=result_name) #result 값을 그리는 그래프 레이블 설정
plt.legend() #범례표기
plt.show()  


# In[ ]:




