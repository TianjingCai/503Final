#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:25:02 2018

@author: Tianjing Cai
"""
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
##install wordcloud
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
Rawfilename="TwitterResultsRelevant.txt"

#Rawfilename="RawWordsStock.txt"
#Freqfilename="BagOfWords.txt"
# Read the whole text.
text = open(path.join(d, Rawfilename)).read()
print(text)
## --OR --
##with open("constitution.txt") as f:
##    lines f.readlines()                                                                            
##text = "".join(lines) 
##---------
wordcloud = WordCloud().generate(text)
# Open a plot of the generated image.
plt.figure(num =1, figsize=(5, 5), dpi=120)
plt.imshow(wordcloud)
plt.axis("off")

plt.savefig('../dataset/alcohol_wordcloud.png')
