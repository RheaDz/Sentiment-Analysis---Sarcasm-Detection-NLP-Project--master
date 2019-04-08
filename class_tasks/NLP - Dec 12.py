
# coding: utf-8

# In[1]:


import nltk
nltk.download()


# In[2]:


from nltk.corpus import brown


# In[6]:


#BROWN CORPUS


# In[3]:


brown.categories()


# In[4]:


brown.words(categories= 'government')


# In[5]:


brown.words(categories= 'government')[:20]


# In[7]:


#INAUGURAL CORPUS


# In[8]:


from nltk.corpus import inaugural


# In[9]:


inaugural.fileids()


# In[10]:


inaugural.words(fileids = '2009-Obama.txt')


# In[11]:


inaugural.words(fileids = '2009-Obama.txt')[:23]

