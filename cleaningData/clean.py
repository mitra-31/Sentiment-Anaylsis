import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def cleanData(tweet):
    return " ".join(re.sub("(@[a-zA-Z0-9]+)|([^0-9A-Za-z])|(https://[\w.]+/[\w]+)"," ",tweet).split())


def dropNumbers(tweet):
    list_text_new = []
    
    for i in tweet:
        if not re.search("\d",i):
            list_text_new.append(i)
    return ''.join(list_text_new)

def lower_case(text):
    text_words = word_tokenize(text)
    text_words_lower = [x.lower() for x in text_words]
    return " ".join(text_words_lower)


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