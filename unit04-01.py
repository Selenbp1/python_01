#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.plot([10,20,30,40])
plt.show()


# In[2]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [12,43,25,15])
plt.show()


# In[3]:


import matplotlib.pyplot as plt
plt.title('plotting')
plt.plot([10,20,30,40])
plt.show()


# In[9]:


import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10,20,30,40], label='asc')
plt.plot([40,30,20,10], label='desc')
plt.legend()
plt.show()


# In[12]:


import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10,20,30,40], label='asc')
plt.plot([40,30,20,10], label='desc')
plt.legend(loc=5)
plt.show()


# In[13]:


import matplotlib.pyplot as plt
plt.title('color')#제목설정
plt.plot([10,20,30,40],color='skyblue', label='skyblue')
plt.plot([40,30,20,10],'pink', label='pink')
plt.legend()#범례표시
plt.show()


# In[23]:


import matplotlib.pyplot as plt
plt.title('linestyle')#제목설정
#빨간색 dashed 그래프
plt.plot([10,20,30,40],'r-', label='dashed')
#초록색 dotted 그래프 
plt.plot([40,30,20,10],'g:', label='dotted')
plt.legend()#범례표시
plt.show()


# In[25]:


import matplotlib.pyplot as plt
plt.title('marker')#제목설정
#빨간색 원형 마커 그래프
plt.plot([10,20,30,40],'r.', label='circle')
#초록색 삼각형 마커 그래프 
plt.plot([40,30,20,10],'g^', label='triangle up')
plt.legend()#범례표시
plt.show()


# In[ ]:




