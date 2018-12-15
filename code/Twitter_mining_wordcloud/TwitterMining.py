#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:13:01 2018

@author: Tianjing Cai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 3 14:41:54 2018

@author: Tianjing Cai
"""

#TwitterMining.py
## Using the Twitter API and Tweepy to 
## gather Twitter data and place tweets to file

## USAGE ##
## This program will ask for a "#something" such as #womensrights
## or #stockmarket. 
## It will then ask for the number of tweets you want to get
## It will OUTPUT a file called:
## hfilename="file_"+nohashname+".txt"
## For example, if you input #womensrights, it will 
## create a file called file_womensrights.txt
## where the tweets will be placed. 
## From here you can call the next program called
## TweepyJSONReader.py


###Packages-----------------------

import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys
###-----------------------------------------


## Create all the keys and secrets that you get
## from using the Twitter API-------------------------------------
consumer_key = 'ghvrVWrqXkXtMG08ZMIo0B3qt'
consumer_secret = 'M8uEhBw5AkbXdd77Rnl2kxU8WfqZu2Nk4afwvhthegwaPMcjsA'
access_token = '1694513684-sGd8G89QsDJStmgYgTHBkw8tOuKNeHxhM0oWWtR'
access_secret = 'krJ4QliSqHlF5FY3gL6LOvLxuxsAanx0ziokqTM6XDwhl'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
##-----------------------------------------------------------------
#Other Tweepy options - FYI
#for status in tweepy.Cursor(api.home_timeline).items(10):
#Process a single status
 #   print(status.text) 
#   
#def Gather(tweet):
 #   print(json.dumps(tweet))
#for friend in tweepy.Cursor(api.friends).items():
 #   Gather(friend._json)
#--------------------------------------------------------------

 
class Listener(StreamListener):
    print("In Listener...") 
    tweet_number=0
    #__init__ runs as soon as an instance of the class is created
    def __init__(self, max_tweets, hfilename, rawfile):
        self.max_tweets=max_tweets
        print(self.max_tweets)     
    #on_data() is a function of StreamListener as is on_error and on_status    
    def on_data(self, data):
        self.tweet_number+=1 
        #print("In on_data", self.tweet_number)
        try:
            #print("In on_data in try")
            with open(hfilename, 'a') as f:
                with open(rawfile, 'a') as g:
                    tweet=json.loads(data)
                    tweet_text=tweet["text"]
                    print(tweet_text,"\n")
                    f.write(tweet_text) # the text from the tweet
                    json.dump(tweet, g)  #write the raw tweet
        except BaseException:
            print("NOPE")
            pass
        if self.tweet_number>=self.max_tweets:
            sys.exit('Limit of '+str(self.max_tweets)+' tweets reached.')
    #method for on_error()
    def on_error(self, status):
        print("ERROR")
        if(status==420):
            print("Error ", status, "rate limited")
            return False
        
hashname=input("Enter the hash name, such as #womensrights: ") 
numtweets=eval(input("How many tweets do you want to get?: "))
nohashname = ''
if numtweets > 30:
    numtweets = eval(input("The number of tweets you want to collect exceed the limit, \nplease enter a value less than or equal to 30: "))
if(hashname[0]=="#"):
    nohashname=hashname[1:] #remove the hash
else:
    hashname = input("Enter the hash name, starting with # sign: ")
    

#Create a file for any hash mine    
hfilename="file_"+nohashname+".txt"
rawfile="file_rawtweets_"+nohashname+".txt"
twitter_stream = Stream(auth, Listener(numtweets, hfilename, rawfile))
#twitter_stream.filter(track=['#womensrights'])
twitter_stream.filter(languages=["en"],track=[hashname])


