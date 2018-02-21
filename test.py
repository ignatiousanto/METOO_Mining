import pandas as pd
import numpy as np
import pickle
import os
from textblob import TextBlob



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

l_o_ass = []
l_o_vic = []
keywords= ["i was","yr", "yrs" "year","years" ]
for i in range(len(body)):
    if any(x in body[i].lower() for x in keywords):
        l_o_ass.append(body[i])
        l_o_vic.append(handle[i])

print(len(l_o_ass),len(l_o_vic))

for i in range(20):
    print(l_o_ass[i],l_o_vic[i])
    blob = TextBlob(l_o_ass[i])
    print(blob.tags)
    print(blob.noun_phrases)





#"yr", "yrs" "year","years","1","2","3","4","5","6", "7","8","9","0" , "grope", "groped", "rape"
