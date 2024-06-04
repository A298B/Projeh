#!/usr/bin/env python
# coding: utf-8

# In[14]:


#پروژه به دست آوردن تعداد کلمات یک رشته
txt="amir hosein is a programmer in iran"
def num(txt):
    x=0
    for i in txt:
        if(i==" "):
            x=x+1
    x=x+1
    return x
print("تعداد کلمات رشته موردنظر برابر است با:", num(txt))


# In[ ]:




