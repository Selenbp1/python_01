#!/usr/bin/env python
# coding: utf-8

#13.숫자 데이터를 쉽게 다루게 돕는 numpy 라이브러리

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()


# In[2]:


import matplotlib.pyplot as plt
t=[]
p2=[]
p3=[]
for i in range(0,50,2):
    t.append(i/10)
    p2.append((i/10)**2)
    p3.append((i/10)**3)
plt.plot(t,t,'r--',t,p2,'bs',t,p3,'g^')
plt.show()


# In[3]:


import numpy
print(numpy.sqrt(2))


# In[4]:


import numpy as np
print(np.sqrt(2))


# In[5]:


import numpy as np 
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))


# In[6]:


import numpy as np
a = np.random.rand(5)
print(a)
print(type(a))


# In[7]:


import numpy as np
print(np.random.choice(6,10))


# In[8]:


import numpy as np
print(np.random.choice(10,6,replace=False))


# In[9]:


import numpy as np
print(np.random.choice(6, 10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1]))


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6, 10)

plt.hist(dice, bins =6)
plt.show()


# In[11]:


import matplotlib.pyplot as plt
import random
dice = []
for i in range(10) :
    dice.append(random.randint(1,6))
plt.hist(dice, bins = 6)
plt.show()


# In[16]:


import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6, 1000000, p=[0.1,0.2,0.3,0.2,0.1,0.1])
plt.hist(dice, bins=6)  # 0, 1, 2, 3, 4, 5 중 랜덤으로 추출한 숫자를 히스토그램 표현
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import random
 
x = []
y = []
size = []
 
for i in range(200) :
    x.append(random.randint(10,100))
    y.append(random.randint(10,100))
    size.append(random.randint(10,100))
 

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()


# In[25]:


import numpy as np
a = np.array([1,2,3,4])
print(a)


# In[26]:


import numpy as np
a = np.array([1,2,3,4])
print(a[1], a[-1])  # a의 1번 인덱스 값, -1번 인덱스 값 출력
print(a[1:])        # a의 1번 인덱스를 기준으로 슬라이싱 결과 출력


# In[28]:


import numpy as np
a = np.array([1,2,'3',4])
print(a)


# In[29]:


import numpy as np
a = np.zeros(10)  # 0으로 이루어진 크기가 10인 배열 생성
print(a)


# In[30]:


import numpy as np
a = np.ones(10)   # 1로 이루어진 크기가 10인 배열 생성
print(a)


# In[31]:


import numpy as np
a = np.eye(3)  # 3행 x 3열의 단위 배열 생성
print(a)


# In[33]:


import numpy as np
a = np.eye(5)  # 5행 x 5열의 단위 배열 생성
print(a)


# In[34]:


import numpy as np
print(np.arange(3))     # arange( ) 함수에 1개 값 입력
print(np.arange(3,7))   # arange( ) 함수에 2개 값 입력
print(np.arange(3,7,2)) # arange( ) 함수에 3개 값 입력


# In[35]:


import numpy as np
a = np.arange(1, 2, 0.1)   # 1이상 2미만 구간에서 0.1 간격으로 실수 생성
b = np.linspace(1, 2, 11)  # 1부터 2까지 11개 구간으로 나눈 실수 생성
print(a)
print(b)


# In[36]:


import numpy as np
a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20)
print(a)
print(b)


# In[37]:


import numpy as np
a = np.zeros(10) + 5
print(a)


# In[38]:


import numpy as np
a = np.linspace(1, 2, 11)
print(np.sqrt(a))  # a값의 제곱근을 출력함


# In[39]:


import matplotlib.pyplot as plt
import numpy as np
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()


# In[40]:


import matplotlib.pyplot as plt
import numpy as np
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()


# In[41]:


import numpy as np
a = np.arange(-5, 5)
print(a)


# In[42]:


print(a<0)


# In[44]:


import numpy as np
a = np.arange(-5, 5)
print(a[a<0])


# In[45]:


mask1 = abs(a) > 3 #abs(a) > 3은 a 배열에 저장된 원소의 절대값이 3보다 크다
print(a[mask1])


# In[46]:


mask1 = abs(a) > 3
mask2 = abs(a) % 2 == 0
print(a[mask1+mask2])   # 둘 중 하나의 조건이라도 참일 경우
print(a[mask1*mask2])   # 두 가지 조건이 모두 참일 경우


# In[55]:


import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(-100, 100, 1000) # 1000개의 랜덤 값 추출
y = np.random.randint(-100, 100, 1000) # 1000개의 랜덤 값 추출
size = np.random.rand(100) * 100
mask1 = abs(x) > 50            # x에 저장된 값 중 절댓값이 50보다 큰 값 걸러 냄
mask2 = abs(y) > 50            # y에 저장된 값 중 절댓값이 50보다 큰 값 걸러 냄
x = x[mask1+mask2]             # mask1과 mask2 중 하나라도 만족하는 값 저장
y = y[mask1+mask2]  # mask1과 mask2 중 하나라도 만족하는 값 저장
size = np.random.rand(len(x)) * 100
plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()


# In[ ]:




