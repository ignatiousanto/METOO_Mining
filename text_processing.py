import pandas as pd
import numpy as np
import pickle
import os
import nltk
# lmtzr = WordNetLemmatizer()
#
#
# folder = './docs'
# df_all = pd.DataFrame()
# comments=[]
# users = []
# time = []
# print(folder)
# for r,s,f in os.walk(folder):
#     print(r)
#     for doc in f:
#         fpath = os.path.join(r,doc)
#         print(fpath)
#         df = pd.read_excel(fpath)
#         df.columns = ["handle","body","link","ts"]
#         comments.append(df["body"].tolist())
#         users.append(df["handle"].tolist())
#         time.append(df["ts"].tolist())
#
# # print(len(comments))
# body = ([item for sublist in comments for item in sublist])
# handle = ([item for sublist in users for item in sublist])
# ts = ([item for sublist in time for item in sublist])
#
# # print(body)
# # print (ts)
# print(len(body),len(handle),len(ts))
#
#
# cleaned_body=[]
# l_o_links=[]
# l_o_hashtags=[]
# l_o_refs=[]
# for tweet in body:
#     cleaned_tweet = []
#     tweet_links=[]
#     tweet_ref=[]
#     tweet_hasht=[]
#     for word in tweet.split():
#         if word[0]=="#":
#             tweet_hasht.append(word)
#         elif word.find("http") != -1:
#             tweet_links.append(word)
#         elif word[0] =="@":
#             tweet_ref.append(word)
#         else :
#             #lemmatizing the word before adding to list
#             print(word)
#             word=lmtzr.lemmatize(word)
#             print("~"+ word)
#             cleaned_tweet.append(word)
#     cleaned_body.append(cleaned_tweet)
#     l_o_refs.append(tweet_ref)
#     l_o_links.append(tweet_links)
#     l_o_hashtags.append(tweet_hasht)
#
#
# print(cleaned_body)
# pickle.dump( [cleaned_body,l_o_links,l_o_refs,l_o_hashtags], open( "save.p", "wb" ) )
load_data = pickle.load( open( "save.p", "rb" ) )

cleaned_body=load_data[0]

##making a flat list of lowercase
flat_list = []
for i in cleaned_body:
    for j in i:
        flat_list.append(j.lower())

stop_words = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some","for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than","rt","&amp;"]
#
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# example_sent = "This is a sample sentence, showing off the stop words filtration."
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(example_sent)
# print(word_tokens)
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# filtered_sentence = []
#
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(word_tokens)
# print(filtered_sentence)

# Remove stopwords
final_bag_of_words = [word for word in flat_list if word not in stop_words]

# Calculate frequency distribution
fdist = nltk.FreqDist(final_bag_of_words)

txt_out = open("top50.txt", "w")
for word, frequency in fdist.most_common(50):
    print(u'{};{}'.format(word, frequency))
    txt_out.write(word+","+str(frequency)+"\n")
txt_out.close()
