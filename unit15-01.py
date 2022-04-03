#!/usr/bin/env python
# coding: utf-8

# In[1]:


#15.테이블 형태의 데이터를 쉽게 다루도록 도와주는 pandas 라이브러리


#국가별 하계 및 동계 올림픽 메달 획득 결과표
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
print(df)


# In[16]:


#국가별 하계 및 동계 올림픽 메달 획득 결과표
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',header=0,index_col=0) #맨 위의 헤더를 열 이름으로 정하고, 나라 이름을 인덱스 이름 적용
# 데이터 중 하계올림픽에 대한 데이터만 추출
summer = df[1].iloc[:,:5]
summer.columns=['경기수','금','은','동','계']
print(summer.sort_values('금', ascending=False)) #sort_values에서 ascending 속성을 변경함으로써 정렬
#만약 오름차순으로 정렬하고 싶으면 False를 True 변경
summer.to_excel('하계올림픽메달.xlsx')


# In[17]:


#pandas는 panel datas(패널 자료)의 약자
#1차원 배열 형태의 데이터 구조를 Series라고 부르고, 2차원 배열 형태의 데이터 구조를 DataFrame
#2차원 배열 형태의 데이터 프레임은 행과 열이 있고, 행을 구분해주는 인덱스(index)와 열을 구분해주는 컬럼(column)이 있음
#별도로 지정해주지 않으면 인덱스는 리스트처럼 정수로 설정이 되고 한 번 설정된 인덱스는 변경되지 않음


# In[19]:


import pandas as pd
index = pd.date_range('1/1/2000', periods=8)
print(index)


# In[20]:


import numpy as np
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df


# In[21]:


#B라는 이름의 특정 열을 선택하였더니,
#날짜로 이루어진 인덱스와 1차원 배열 형태(시리즈 형태)로 값이 출력되는 것을 확인
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B'])


# In[22]:


#B 열의 데이터가 0.4보다 큰 지 확인하는 조건
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B']>0.4)


# In[23]:


#B열의 값이 0.4보다 큰 값이라는 조건이 True인 데이터들로만 이루어진 데이터 프레임
#T는 행과 열을 바꾼다는 의미의 단어 transpose를 의미
#행 방향 축을 기준으로 한 연산
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D']=df['A']/df['B'] #A열의 값을 B열의 값으로 나눈 값을 D열에 저장
df


# In[26]:


#열 방향 축을 기준으로 계산
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D']=df['A']/df['B']
df['E'] = np.sum(df, axis=1) # 행 우선 계산 값을 E열에 저장
df.head() #head() 함수는 많은 데이터 중 처음 5개의 데이터만 확인하고 싶을 때 사용하는 함수


# In[28]:


#전체 데이터를 A열의 값으로 뺄 때는 sub() 함수를 사용
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D']=df['A']/df['B']
df['E'] = np.sum(df, axis=1)
df=df.sub(df['A'],axis=0) #A열의 데이터를 기준으로 열 우선 계산
df.head()


# In[29]:


#데이터 전체를 C열 값으로 나눌 때는 div() 함수를 사용
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D']=df['A']/df['B']
df['E'] = np.sum(df, axis=1)
df=df.sub(df['A'],axis=0) 
df=df.div(df['C'],axis=0) #C열 데이터를 기준으로 열 우선 계산
df.to_csv('test.csv') #데이터 프레임을 test.csv 파일로 저장
df.head()


# In[46]:


#1 | 데이터를 읽어온다.
    #➊ 전체 데이터를 총 인구수로 나누어 비율로 변환한다.
    #➋ 총인구수와 연령구간인구수를 삭제한다.
#2 | 궁금한 지역의 이름을 입력받는다.
#3 | 궁금한 지역의 인구 구조를 저장한다.
#4 | 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    #➊ 전국의 모든 지역 중 한 곳(B)을 선택한다.
    #➋ 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 뺀다.
    #➌ ➋를 100세 이상 인구수에 해당하는 값까지 반복한 후 차이의 제곱을 모두 더한다.
    #➍ 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.
#5 | 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다.

import pandas as pd
df = pd.read_csv('age.csv', encoding='utf8', index_col=1)
df = df.div(df['총 인구수'], axis=0) # 1 │ ➊ 전체 데이터를 총인구수로 나눠서 비율로 변환
del df['행정기관코드'], df['총 인구수'], df['연령구간인구수']  # 1 │ ➋ 총인구수, 연령구간인구수 열 삭제

name = input('원하는 지역의 이름을 입력해주세요 : ')  # 2 │ 지역 이름 입력
a = df.index.str.contains(name)  # 3 │ 해당 행을 찾아서 해당 지역의 인구 구조를 저장
df2 = df[a]

import numpy as np
# 4 │ ➊ 궁금한 지역 A의 인구 비율에서 B의 인구 비율을 뺀다.
x = df.sub(df2.iloc[0], axis=1) #iloc - 행 번호를 기준으로 행 데이터 읽기
# 4 │ ➋ A의 인구 비율에서 B의 인구 비율을 뺀 값의 제곱 값을 모두 더한다.
y = np.power(x, 2)
z = y.sum(axis=1)
i = z.sort_values().index[:5]  # 4 │ ➌ 그 차이가 가장 작은 지역 5곳을 찾는다.

import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
df.loc[i].T.plot()   # 4 │ ➍ 결과를 꺾은선 그래프로 보여준다.
plt.show()


# In[23]:


#1 | 데이터를 읽어온다.
    #➊ 전체 데이터를 총 인구수로 나누어 비율로 변환한다.
    #➋ 총인구수와 연령구간인구수를 삭제한다.
#2 | 궁금한 지역의 이름을 입력받는다.
#3 | 궁금한 지역의 인구 구조를 저장한다.
#4 | 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    #➊ 전국의 모든 지역 중 한 곳(B)을 선택한다.
    #➋ 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 뺀다.
    #➌ ➋를 100세 이상 인구수에 해당하는 값까지 반복한 후 차이의 제곱을 모두 더한다.
    #➍ 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.
#5 | 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
df = pd.read_csv('age.csv', encoding='utf8', index_col=1)
df = df.div(df['총 인구수'], axis=0) # 1 │ ➊ 전체 데이터를 총인구수로 나눠서 비율로 변환
del df['행정기관코드'], df['총 인구수'], df['연령구간인구수']  # 1 │ ➋ 총인구수, 연령구간인구수 열 삭제

name = input('원하는 지역의 이름을 입력해주세요 : ')  # 2 │ 지역 이름 입력
a = df.index.str.contains(name)  # 3 │ 해당 행을 찾아서 해당 지역의 인구 구조를 저장
df2 = df[a]

# 4 │ 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기
df.loc[np.power(df.sub(df2.iloc[0], axis=1), 2).sum(axis=1).sort_values().index[:6]].T.plot()

plt.show()



