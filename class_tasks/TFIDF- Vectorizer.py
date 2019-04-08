
# coding: utf-8

# In[14]:


import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
stemmer=PorterStemmer()
doc1="HOW DEEP IS YOUR LOVE? If there is a phrase I would prefer to retire from online bios, personal or professional, it is, \"I love travel.\" Or some approximation of that sentiment. To clarify, I am not against travellers or those who proudly flaunt their passion for travel. On the contrary, editing a travel magazine has now made me oddly protective of travellers and their ilk. My submission is that \"love to travel,\" suggested so casually, just doesn't feel adequate to the depth of emotion it sparks in true devotees. In February, the month of love as endowed by our great gifting industrial complex, we are wrestling with what \"love for travel\" means in tangible, life-affecting terms. The early throes of discovering travel might not be too dissimilar to the beginnings of a feverish affair."
doc1=[stemmer.stem(token) for token in doc1.split(" ")]
doc2="Summer is a charming flirt. Easy-going and casual. Summer doesn't huff and puff to win our affections. It has us at \"Hello.\" Winter broods like the tortured protagonist of big fat Russian novel. It is daunting and dramatic, burning with a slow intensity. The season's reputation precedes itself, and often, not in a good way. It has a way of whitting down everything to its bare bones. Even relationships not attuned to its ebbs and flows can fray. At a dinner converesation I once attended, I listened in bemusement as a recent divorcee made the case that it was the Scandinavian frost that had cooled his ex-wife's ardour. How original."
doc2=[stemmer.stem(token) for token in doc2.split(" ")]
#corpus=[doc1,doc2]
corpus=[" ".join(doc1)," ".join(doc2)]
vect=CountVectorizer(binary=True)
print(corpus)
vect.fit(corpus)
#sim=cosine_similarity(vect.transform([doc1]).toarray(),vect.transform([doc2]).toarray())
sim=cosine_similarity(vect.transform([" ".join(doc1)]).toarray(),vect.transform([" ".join(doc2)]).toarray())
print(vect.vocabulary_)
print(sim)




# In[ ]:


















 nm,.

