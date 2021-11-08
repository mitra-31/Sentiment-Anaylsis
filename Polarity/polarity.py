from textblob import TextBlob





def get_polarity(text):
    textblob = TextBlob(str(text))
    pol = textblob.sentiment.polarity
    
    if(pol==0):
        return "Neutral"
    elif(pol >0 and pol <= 0.3):
        return "Weakly Positive"
    elif(pol >0.3 and pol <= 0.6):
        return "Positive"
    elif(pol>0.6 and pol<=1):
        return "Strongly Positive"
    elif(pol>-0.3 and pol<=0):
        return "Weakly Negative"
    elif(pol>-0.6 and pol<=-0.3):
        return "Negative"
    elif(pol>-1 and pol<=-0.6):
        return "Strongly Negative"
    
def get_polarity_values(dataframe):
    values = {"neutral":0,
    "wpos":0,
    "spos":0,
    "pos":0,
    "neg":0,
    "wneg":0,
    "sneg":0,
    "polarity":0}
    for i in range(0, len(dataframe["Cleaned_Data"])):
        textblob = TextBlob(str(dataframe["Cleaned_Data"][i]))
        values["polarity"] += textblob.sentiment.polarity
        pol = textblob.sentiment.polarity

        if(pol==0):
            values["neutral"] += 1
        elif(pol >0 and pol <= 0.3):
            values["wpos"] += 1
        elif(pol >0.3 and pol <= 0.6):
            values["pos"] += 1
        elif(pol>0.6 and pol<=1):
            values["spos"] += 1
        elif(pol>-0.3 and pol<=0):
            values["wneg"] += 1
        elif(pol>-0.6 and pol<=-0.3):
            values["neg"] += 1
        elif(pol>-1 and pol<=-0.6):
            values["sneg"] += 1
    return values

def getAvgPolarity(polarity,totalTweets):
    pass