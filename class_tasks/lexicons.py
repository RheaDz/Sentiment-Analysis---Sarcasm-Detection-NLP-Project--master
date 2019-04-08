
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords
words=set(stopwords.words('english'))
print(words)


# In[2]:


len(words)


# In[3]:


import nltk

word = input('Enter any word:')
from nltk.corpus import wordnet as wn
id = str(wn.synsets(word))

print('The id of the word', word, 'is: ', id)

wordsyn = id[9:len(id)-3]
print('\nThe synonyms of the word', word, 'are: ')
print(wn.synset(wordsyn).lemma_names())


# In[4]:


import nltk

word = input('Enter any word:')
from nltk.corpus import wordnet as wn
id = wn.synsets(word)


for i in range(0, len(id)-1):    
    id_num = str(id[i])
    wordsyn = id_num[8:len(id_num)-3]
    print('\nThe synonyms of the word', word, 'for id num', i, '-', id[i], 'are:')
    print(wn.synset(wordsyn).lemma_names(), '\n')

