import tweepy
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from textblob import TextBlob
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

auth = tweepy.OAuthHandler()
auth.set_access_token()

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# searchTerm = input("Enter Keyword/Tag to search abiut: ")




tweets = []
tweetText = []

# tweets = tweepy.Cursor(api.search, q=searchTerm+" -filter:retweets",lang="en").items(6)

tweets = api.search_tweets(q="Sharuk Khan"+" -filter:retweets",lang="en")
tweet_list = [tweet.text for tweet in tweets]
tweet_df = pd.DataFrame(tweet_list)




lemmatizer = WordNetLemmatizer()

def lemmatise(text):
    text_tokens = word_tokenize(text)
    text_lemm = [lemmatizer.lemmatize(word) for word in text_tokens]
    return " ".join(text_lemm)

def removingStopWords(text):
    text_tokens = word_tokenize(text)
    tokens = [word for word in text_tokens if not word in set(stopwords.words('english'))]
    token_text = " ".join(tokens)
    return token_text



tweet_df["Cleaned_Data"] = tweet_df[0].apply(cleanData)
tweet_df["Cleaned_Data"] = tweet_df["Cleaned_Data"].apply(dropNumbers)
tweet_df["Cleaned_Data"] = tweet_df["Cleaned_Data"].apply(lower_case)
tweet_df["Cleaned_Data"] = tweet_df["Cleaned_Data"].apply(lemmatise)
tweet_df["Cleaned_Data"] = tweet_df["Cleaned_Data"].apply(removingStopWords)
tweet_df["polarity"] = tweet_df["Cleaned_Data"].apply(get_polarity)



neutral = 0
wpos = 0
spos = 0
pos = 0
neg = 0
wneg = 0
sneg = 0
polarity = 0


for i in range(0, len(tweet_df["Cleaned_Data"])):
    textblob = TextBlob(str(tweet_df["Cleaned_Data"][i]))
    polarity += textblob.sentiment.polarity
    pol = textblob.sentiment.polarity
    
    if(pol==0):
        neutral += 1
    elif(pol >0 and pol <= 0.3):
        wpos += 1
    elif(pol >0.3 and pol <= 0.6):
        pos += 1
    elif(pol>0.6 and pol<=1):
        spos += 1
    elif(pol>-0.3 and pol<=0):
        wneg += 1
    elif(pol>-0.6 and pol<=-0.3):
        neg += 1
    elif(pol>-1 and pol<=-0.6):
        sneg += 1
        

#Avg

polarityAvg = polarity/len(tweets)
print(polarityAvg)


def percentage(part,whole):
    temp = 100*float(part)/float(whole)
    return format(temp,".2f")

print(percentage(pos,len(tweets)))