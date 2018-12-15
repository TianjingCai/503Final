#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 4 15:06:49 2018

@author: Tianjing Cai
"""

# -*- coding: utf-8 -*-



#TweepyJSONReader.py
##Reads JSON files of tweets that Tweepy collects
#Gates

##This program will read a .txt file
## that was created by TwitterMining.py
## Set the filename correctly

## This program will create two files:
## "TwitterResultsRaw.txt" which is all the words
## "TwitterWordFrq.txt" which is each word and its frequency


import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re
#https://docs.python.org/3/library/re.html

linecount=0
hashcount=0
wordcount=0
BagOfWords=[]
BagOfHashes=[]
BagOfLinks=[]

### SET THE FILE NAME ###

tweetsfile="file_Alcohol.txt"

###################################

with open(tweetsfile, 'r') as file:
    for line in file:
        #print(line,"\n")
        tweetSplitter = TweetTokenizer(strip_handles=True, reduce_len=True)
        WordList=tweetSplitter.tokenize(line)
        #WordList2=word_tokenize(line)
        #linecount=linecount+1
        #print(WordList)
        #print(len(WordList))
        #print(WordList[0])
        #print(WordList2)
        #print(len(WordList2))
        #print(WordList2[3:6])
        #print("NEXT..........\n")
        regex1=re.compile('^#.+')
        regex2=re.compile('[^\W\d]') #no numbers
        regex3=re.compile('^http*')
        regex4=re.compile('.+\..+')
        for item in WordList:
            if(len(item)>2):
                if((re.match(regex1,item))):
                    #print(item)
                    newitem=item[1:] #remove the hash
                    BagOfHashes.append(newitem)
                    hashcount=hashcount+1
                elif(re.match(regex2,item)):
                    if(re.match(regex3,item) or re.match(regex4,item)):
                        BagOfLinks.append(item)
                    else:
                        BagOfWords.append(item)
                        wordcount=wordcount+1
                else:
                    pass
            else:
                pass
            
    
        
       
#print(linecount)            
#print(BagOfWords)
#print(BagOfHashes)
#print(BagOfLinks)
BigBag=BagOfWords+BagOfHashes




#list of words I have seen
seenit=[]
#dict of word counts
WordDict={}
Rawfilename="TwitterResultsRelevant.txt"
Freqfilename="TwitterWordFrq.txt"


#FILE=open(Freqfilename,"w")
#FILE2=open(Rawfilename, "w")

# File that store words after filtering
R_FILE=open(Rawfilename,"w")

# File that store words and their appearing frequency
F_FILE=open(Freqfilename, "w")

# Create a list of words to ignore
IgnoreThese=["and", "And", "AND","THIS", "This", "this", "for", "FOR", "For", 
             "THE", "The", "the", "is", "IS", "Is", "or", "OR", "Or", "will", 
             "Will", "WILL",  "still", "Still", "Need", "need", "food", "Food", "Flint", 
             "Webchat",  "fifdh17", "But", "but", "Has", "has", "about", "with", "all", "I", "you", "your", "his", "her", 
             "ser", "its", "put", "just"]
# Remove stopwords of different languages for tweets 
IgnoreThese = IgnoreThese + stopwords.words('english')
IgnoreThese = IgnoreThese + stopwords.words('dutch')
IgnoreThese = IgnoreThese + stopwords.words('spanish')
IgnoreThese = IgnoreThese + stopwords.words('french')
###Look at the words
for w in BigBag:
    if(w not in IgnoreThese):
        rawWord=w+" "
        R_FILE.write(rawWord)
        if(w in seenit):
            #print(w, seenit)
            WordDict[w]=WordDict[w]+1 #increment the times word is seen
        else:
            ##add word to dict and seenit
            seenit.append(w)
            WordDict[w]=1
    
#print(WordDict)  
#print(seenit)
#print(BagOfWords)


# Create a word, frequency document
for key in WordDict:
    #print(WordDict[key])
    if(WordDict[key]>1):
        if(key not in IgnoreThese):
            #print(key)
            Key_Value=key + "," + str(WordDict[key]) + "\n"
            F_FILE.write(Key_Value) # write word and its appearing times into a file if it shows up multiple times


#FILE.close()
#FILE2.close()
R_FILE.close()
F_FILE.close()
