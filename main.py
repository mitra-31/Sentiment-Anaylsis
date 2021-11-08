import tweepy
import pandas as pd

from authentication import authentic as a
from cleaningData import clean
from Polarity import polarity as p


def start():
    # Authentication
    auth = tweepy.OAuthHandler(a.consumer_key,a.consumer_secret)
    auth.set_access_token(a.access_token,a.access_token_secret)
    api = tweepy.API(auth)
    print("Successfully started")
    return api


class TweetsHandler:
    
    def __init__(self, api,tweet_id="Sharuk Khan"):
        self.api = api
        self.tweet_id = tweet_id
        self.tweetsDataframe =  self.get_tweets()
        # self.total_tweets = len(self.tweetsDataframe)
        
        
    def get_tweets(self):
        tweets = []
        # tweetText = []
        # tweets = tweepy.Cursor(api.search, q=searchTerm+" -filter:retweets",lang="en").items(6)
        tweets = self.api.search_tweets(q=self.tweet_id+" -filter:retweets",lang="en")
        tweet_list = [tweet.text for tweet in tweets]
        tweet_df = pd.DataFrame(tweet_list)
        print(tweet_df,"Hlll")
        return tweet_df
    
    def clean_tweets(self):
        self.tweetsDataframe["Cleaned_Data"] = self.tweetsDataframe[0].apply(clean.cleanData)
        self.tweetsDataframe["Cleaned_Data"] = self.tweetsDataframe["Cleaned_Data"].apply(clean.dropNumbers)
        self.tweetsDataframe["Cleaned_Data"] = self.tweetsDataframe["Cleaned_Data"].apply(clean.lower_case)
        self.tweetsDataframe["Cleaned_Data"] = self.tweetsDataframe["Cleaned_Data"].apply(clean.lemmatise)
        self.tweetsDataframe["Cleaned_Data"] = self.tweetsDataframe["Cleaned_Data"].apply(clean.removingStopWords)
        self.tweetsDataframe["polarity"] = self.tweetsDataframe["Cleaned_Data"].apply(p.get_polarity)
        
    def get_tweets(self):
        pass
    
    def get_polarity(self):
        values = p.get_polarity_values(self.tweetsDataframe)
        return values

    def get_average_polarity(self):
        avg = self.get_polarity()["polarity"]/self.total_tweets
        return avg
    
        
    
    
    

if __name__ == "__main__":
    
    ## Initilizing Class
    api = start()
    tweets = TweetsHandler(api)
    
    ## Cleaning the Data
    tweets.clean_tweets()
    
    ## Printing the retrived data from twitter
    print(tweets.tweetsDataframe)
    
    ## Get Polarity values
    for key,values in tweets.get_polarity().items():
        print(key," ",values)
    