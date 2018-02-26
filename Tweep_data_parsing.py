#tweep_Data_parsing
import guess_language
import pickle
f = open('./oct_out.txt', 'r')

l_id=[]
l_date=[]
l_time=[]
l_usr=[]
l_body=[]

for line in f:
    working = line.split(" ",5)
    if len(working) != 6:
        print(working)
    elif guess_language.guess_language(working[5]) == 'en':
        l_id.append(working[0])
        l_date.append(working[1])
        l_time.append(working[2])
        l_usr.append(working[4])
        l_body.append(working[5])
    # else :
    #     print(working[5])
    #     print(guess_language.guess_language(working[5]))
    #     print("#"*20)
f.close()
f = open('./test2.txt', 'r')
for line in f:
    working = line.split(" ",5)
    if len(working) != 6:
        print(working)
    elif guess_language.guess_language(working[5]) == 'en':
        l_id.append(working[0])
        l_date.append(working[1])
        l_time.append(working[2])
        l_usr.append(working[4])
        l_body.append(working[5])
f.close()

cleaned_body=[]
l_links=[]
l_hashtags=[]
l_refs=[]
for tweet in l_body:
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
            # #lemmatizing the word before adding to list
            # print(word)
            # word=lmtzr.lemmatize(word)
            # print("~"+ word)
            cleaned_tweet.append(word)
    cleaned_body.append(' '.join(cleaned_tweet))
    l_refs.append(tweet_ref)
    l_links.append(tweet_links)
    l_hashtags.append(tweet_hasht)

print(cleaned_body)

pickle.dump( [l_id,l_date,l_time,l_usr,cleaned_body,l_links,l_refs,l_hashtags], open( "save.p", "wb" ) )
pickle.dump( l_body, open( "body.p", "wb" ) )
