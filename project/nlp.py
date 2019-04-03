import nltk
import re
import enchant
from textblob import TextBlob
import matplotlib.pyplot as plt
import emoji
import pickle
import os
import sklearn
import numpy as np


lemma = nltk.wordnet.WordNetLemmatizer()
d=enchant.Dict("en_US")
use_stemmer=True

f=open("sample1.txt","r")
x=f.readlines()


positive_file=open("abc.txt","r")
q=positive_file.readlines()
z=[]
for i in q:
    z.append(i[0:-1])


negetive_file=open("def.txt","r")
y=negetive_file.readlines()
m=[]
for i in y:
    m.append(i[0:-1])

T_score=[]
T_score1=[]

def pre_tweet(tweet):
    tweet=tweet.lower()
    tweet=re.sub(r'((www\.[\S]+)|(https?://[\S]+))', '', tweet)
    tweet=re.sub(r'@[\S]+', '', tweet)
    tweet1=tweet.split()
    tweet2=TextBlob(tweet)
    t_score=0
    sc=tweet2.sentiment.polarity
    #print(tweet2.tags)
    #print("Score1 : ",sc)
    T_score1.append(sc)
    for words in tweet1:
        if d.check(words)==True:
            word = lemma.lemmatize(words)
            if words in z:
                t_score+=0.5
            if words in m:
                t_score-=0.5
            #print(word,end=' ')
    #print("Score 2 : ",t_score)
    T_score.append(t_score)

        

l=[]
for i in x[0:1000]:
    l.append(pre_tweet(i))

    
print(T_score)
print(T_score1)
p,q,n=0,0,0
for i in T_score:
    if i>0:
        p+=1
    if i<0:
        q+=1
    if i==0:
        n+=1
ts1=[p,q,n]
labels=["positive","negetive","neutral"]
colors=["green","red","blue"]
patches, texts = plt.pie(ts1, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

p,q,n=0,0,0
for i in T_score1:
    if i>0:
        p+=1
    if i<0:
        q+=1
    if i==0:
        n+=1
ts2=[p,q,n]
labels=["positive","negetive","neutral"]
colors=["green","red","blue"]
patches, texts = plt.pie(ts2, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
print("\n")     
print("Percentages Score 1 :")
print("  Positive : ",ts1[0]/(ts1[0]+ts1[1]+ts1[2])*100)
print("  Negetive : ",ts1[1]/(ts1[0]+ts1[1]+ts1[2])*100)
print("  Neutral : ",round(ts1[2]/(ts1[0]+ts1[1]+ts1[2])*100,2))
print("Percentages Score 2 : (TextBlob)")
print("  Positive : ",ts2[0]/(ts2[0]+ts2[1]+ts2[2])*100)
print("  Negetive : ",ts2[1]/(ts2[0]+ts2[1]+ts2[2])*100)
print("  Neutral : ",ts2[2]/(ts2[0]+ts2[1]+ts2[2])*100)
print("\n")

def preprocessing():
    with open('emoji.txt', 'r', encoding='utf16', errors='ignore') as file:
        text = file.read().split('\n')
    for i in range(len(text)):
        text[i] = emoji.demojize(text[i])
    with open('final_tweets.txt', 'w+', encoding='utf8', errors='ignore') as file:
        new_text = ""
        for i in range(len(text)):
            new_text += text[i] + "\n"
        file.write(new_text)

preprocessing()


f=open('final_tweets.txt','r')
zz=f.readlines()
score_emo=0
ZZ=[]
for i in zz:
    ZZ.append(i[0:-1])
sc1=[]
sc2=[]
for i in ZZ:
    score_emo=0
    twe=TextBlob(i)
    dc=twe.sentiment.polarity
    sc1.append(dc*0.1)
    zzz=[]
    zzz=i.split(" ")
    for i in zzz:
        if i==":loudly_crying_face:":
            score_emo+=-0.093
        if i==":face_with_tears_of_joy:":
            score_emo+=0.221
        if i==":winking_face_with_tongue:":
            score_emo+=0.445
        if i==":confused_face:":
            score_emo+=0.001
        if i==":red_heart:":
            score_emo+=0.746
        if i==":angry_face:":
            score_emo+=-0.397
    sc2.append(score_emo)
print(sc1)
print(sc2)
fsc=[]
for i in range(len(sc1)):
    fsc.append(sc1[i]+sc2[i])
#print(fsc)
SC1=np.sign(sc1)
SC2=np.sign(sc2)
SC=[]
Sc=[]
for i in range(len(sc1)):
    if SC1[i]==SC2[i]:
        SC.append(SC1[i])
        Sc.append("no")
    else:
        SC.append(SC2[i])
        Sc.append("yes")
print(SC)
print(Sc)


'''def getSarcasmScore(sentence):
    features = feature_extraction.getallfeatureset(sentence)
    
    features_vec = vec.transform(features)
    score = classifier.decision_function(features_vec)[0]
    percentage = int(round(2.0*(1.0/(1.0+np.exp(-score))-0.5)*100.0))
    
    return percentage

data = "Messi is the best footballer in the world"
print(getSarcasmScore(data))'''
