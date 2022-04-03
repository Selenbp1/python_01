#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#출력과 입력 그리고 변수
#print라는 이름의 함수는 괄호 안의 어떤 값을 모니터에 출력할 때 사용
print(3**2)
print('hello world')

#변수
#변하는 값
#‘name = ‘파이쏭’’ 코드에서 name이 바로 변수이고 = 기호는 오른쪽의 값을 왼쪽에 대입(또는 배정)하는 역할
name = '파이쏭'
print(name)

a = 1024  # 변수의 이름은 지정하면 됨
print(a)

# name 변수의 값을 ‘파이쏭’ 대신 다른 값으로 바꿔보세요!
name = '파이쏭' 
print(name+'님! 안녕하세요!')

#input() 함수로 문자열 값 입력받기
name = input()
print(name+'님! 안녕하세요!')


# In[7]:


#함수(函數, function)는 함(函, 상자 함)의 뜻처럼 상자 안에 값을 넣으면 어떤 기능을 수행
#파이썬에서는 함수 이름 뒤에 소괄호가 열리고 닫히는 형태로 표현
#input이라는 함수는 키보드로 문자열 값을 입력받는 기능을 하는 함수
age = input('나이를 입력해주세요! : ')
print(int(age)-4)

name = input('이름을 입력해주세요 : ')
age = int(input('나이를 입력해주세요 : '))
print('안녕하세요!', name+'님! 저는 처음에 '+str(age - 4)+'살인 줄 알았어요!!')


# In[12]:


#연산자 사용하기
#산술 연산자(arthmetic operator)
print(3 * 10)   # * : 곱셈 연산자
print(3 ** 10)  # ** : 거듭 제곱 연산자
print(3 % 10)   # % : 나머지 연산자
print(3 / 2)    # / : 실수 나눗셈
print(3 // 2)   # // : 정수 나눗셈

#비교 연산자(comparison operator)
print(10 >= 3)
print(10 <= 3)
print(10 == 3)   # == : 같다
print(10 != 3)   # != : 같지 않다
print(3 % 2 == 1)
print('===============')

#논리 연산자(logical operator)
print(1 == 1 and 2 != 1)           # True and True
print(10 % 2 != 0 and 1 + 1 > 0)   # True and False
print(10 < 5 or 10 == 5)          # False or False
print(10 % 2 != 0 or 1 + 1 > 0)   # True or False
print(not 10 > 5)     # not True
print(not 10 == 5)    # not False
print(not 0)          # 0은 False에 해당
print(not 10)         # 0을 제외한 숫자도 True에 해당


# In[13]:


#함수 불러오기
#import random은 random이라는 이름의 라이브러리를 불러오라는 명령이고, 
#random.randint(1,6)은 random 라이브러리에 있는 randint라는 함수에 1과 6을 입력해서 실행하라는 의미
import random
dice = random.randint(1,6)
print(dice)

#제곱근 함수를 사용하려면 math라는 수학 관련 라이브러리를 불러와서 math 라이브러리에 있는 sqrt() 함수를 실행
import math
print(math.sqrt(2))


# In[24]:


#반복과 선택
#for 반복문
#for 반복문은 주어진 데이터 세트를 순회하거나 원하는 횟수만큼 반복하고 싶을 때 사용
#for A in B :          # 맨 뒤에 콜론 기호(:)를 잊지 마세요.
#    반복할 문장1      # 들여쓰기(문단 구분)가 되어 있음
#    (반복할 문장n)    # 보통 공백 문자([space]) 4개로 사용함
name = '파이쏭'
for i in name :
    print(i)
    
names = ['쵸파','루피','상디','조로']
for name in names :
    print(name)

for i in [0,1,2,3] :
    print(i ** 2)

for i in range(100) : # range(100) : 0 이상 100 미만(0, 1, 2, ..., 98, 99)의 범위를 갖는 정수
    print(i ** 2)
    
for i in range(100) :  # 0부터 99까지의 정수 100개 생성. 즉, 100번 반복
    print('나는 파이썬왕이 될 사람이다!!')


# In[25]:


#if 조건문
#if 조건문은 주어진 조건이 True(참)인 경우에만 명령을 선택적으로 실행하고 싶을 때 사용
#if 조건 :                            # 맨 뒤에 ‘:’ 콜론을 잊지 마세요!
#    조건이 참일 경우 실행할 문장1    # 들여쓰기가 되어 있음
#    (조건이 참일 경우 실행할 문장1)  # 들여쓰기를 잊지 마세요!
if 10 > 0 :
    print('안녕하세요?')

if 10 != 0 and 5 % 2 == 1 :
    print('안녕하세요?')

passwd  = int(input('비밀번호 4자리를 입력하세요 : '))
if passwd == 1531 :
    print('비밀번호가 일치합니다.')
    
for i in range(10000) :
    if i == 1531 :                        # 1단계 들여쓰기
        print('비밀번호가 일치합니다.')   # 2단계 들여쓰기


# In[26]:


passwd  = int(input('비밀번호 4자리를 입력하세요 : '))
if passwd == 1531 :
    print('비밀번호가 일치합니다.')
else :
    print('______________________')


# In[27]:


#파이썬 elif
print('[ 소름끼치도록 놀라운 심리테스트 ]')
menu = input('당신이 좋아하는 음식을 입력해주세요 : ')
if menu == '짜장면' :
    print('당신은 짜장면을 좋아하는 사람입니다.')
elif menu == '아이스크림' :
    print('당신은 아이스크림을 좋아하는 사람입니다.')
elif menu == '사탕' :
    print('당신은 사탕을 좋아하는 사람입니다.')
else :
    print('당신은 짜장면과 아이스크림과 사탕을 좋아하지 않는 사람입니다.')


# In[35]:


#순서 있는 저장 공간 리스트
#순서가 있는 데이터를 다룰 때, 리스트(List) 데이터 구조
#인덱스(index)로 리스트의 값에 접근할 수 있다는 것이 리스트의 가장 큰 특징
names = ['쵸파','루피','상디','조로']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

names = ['쵸파','루피','상디','조로']
print(names[-1])  # 인덱스 –1 : 뒤에서 첫 번째 데이터에 접근

#리스트에 저장된 위치로 데이터의 일부 자르기(slicing)
#순서에 따라 여러 데이터에 접근
names = ['쵸파','루피','상디','조로']
print(names[0:2])
print(names[1:3])
print(names[1:])
print(names[:])

#리스트에 값 추가하기
names = ['쵸파','루피','상디','조로']
names.append('나미')  # 리스트에 값 추가하기
print(names)

#리스트에 몇 개의 데이터가 저장되었는지 확인하려면 length라는 뜻의 len() 함수를 사용
print(len(names))                         # 리스트 길이 출력하기
print(len('data analysis for everyone'))  # 문자열 길이 출력하기

names = ['쵸파', '루피', '상디', '조로']
names.append('해적왕')
for name in names :
    if len(name) > 2 :
        print(name,'왔나요~?')


# In[ ]:




