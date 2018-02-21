import pandas as pd
import numpy as np
import pickle
import os

from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()


folder = './docs'
df_all = pd.DataFrame()
comments=[]
users = []
time = []
print(folder)
for r,s,f in os.walk(folder):
    print(r)
    for doc in f:
        fpath = os.path.join(r,doc)
        print(fpath)
        df = pd.read_excel(fpath)
        df.columns = ["handle","body","link","ts"]
        comments.append(df["body"].tolist())
        users.append(df["handle"].tolist())
        time.append(df["ts"].tolist())

# print(len(comments))
body = ([item for sublist in comments for item in sublist])
handle = ([item for sublist in users for item in sublist])
ts = ([item for sublist in time for item in sublist])

# print(body)
# print (ts)
print(len(body),len(handle),len(ts))


cleaned_body=[]
l_o_links=[]
l_o_hashtags=[]
l_o_refs=[]
for tweet in body:
    cleaned_tweet = []
    tweet_links=[]
    tweet_ref=[]
    tweet_hasht=[]
    for word in tweet.split():
        if word[0]=="#":
            tweet_hasht.append(word)
        elif word.find("http") != -1:
            tweet_links.append(word)
        elif word[0] =="@":
            tweet_ref.append(word)
        else :
            #lemmatizing the word before adding to list
            print(word)
            word=lmtzr.lemmatize(word)
            print("~"+ word)
            cleaned_tweet.append(word)
    cleaned_body.append(cleaned_tweet)
    l_o_refs.append(tweet_ref)
    l_o_links.append(tweet_links)
    l_o_hashtags.append(tweet_hasht)


print(cleaned_body)
pickle.dump( [cleaned_body,l_o_links,l_o_refs,l_o_hashtags], open( "save.p", "wb" ) )



# print(df_all)
# print("``"*50)
# print(df_all.head)
