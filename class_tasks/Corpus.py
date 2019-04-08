
# coding: utf-8

# In[1]:


import nltk
nltk.download()


# In[2]:


from nltk.corpus import brown


# In[4]:


print(brown.categories())


# In[5]:


brown.words(categories='romance')


# In[6]:


from nltk.corpus import inaugural


# In[7]:


inaugural.fileids()


# In[8]:


inaugural.words(fileids='1989-Bush.txt')


# In[9]:


inaugural.words(fileids='1989-Bush.txt')[:50]


# In[10]:


from nltk.tokenize import TweetTokenizer
text="Mexico is paying (indirectly) for the Wall through the new USMCA, the replacement for NAFTA! Far more money coming to the U.S. Because of the tremendous dangers at the Border, including large scale criminal and drug inflow, the United States Military will build the Wall!"
twt = TweetTokenizer()
print(twt.tokenize(text))

