
# coding: utf-8

# In[3]:


from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import pos_tag
texts =  ["""The year of birth of Socrates stated is an assumed date,[50] or estimate,[51] given the fact of the dating of anything in ancient history in part being sometimes reliant on argument stemming from the inexact period floruit of individuals.
[52] Diogenes Laërtius stated Socrates birth date was "the sixth day of Thargelion, the day when the Athenians purify the city".
[53] Contemporaneous sources state, he was born not very much later than sometime after the year 471,[54] his date of birth is within the period of years ranging 470 to 469 BC,[55]
or within a range 469 to 468 BC (corresponding to the fourth year of the 77th Olympiad).[36][37]
Socrates was born in Alopeke, and belonged to the tribe Antiochis. His father was Sophroniscus, a sculptor, or stonemason.
[56][57][58] His mother was a midwife named Phaenarete.[59] Socrates married Xanthippe, who is especially remembered for having an undesirable temperament.[60] She bore for him three sons,[61] Lamprocles, Sophroniscus and Menexenus."""]

for sent in texts:
    sentence=sent_tokenize(sent)
    for words in sentence:
        wrd=word_tokenize(words)
        for tag in wrd:
            tagger=pos_tag(wrd)
            print(tagger)
         

