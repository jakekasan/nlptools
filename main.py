from functools import reduce
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_stopwords
from nltk.stem import WordNetLemmatizer

def get_tokens(target=None):
    """
        takes a string or array and returns an array of all words, lowercase 
    """
    if target is None:
        return []

    if type(target) == pd.Series:
        target = reduce(lambda x,y: x+y,target)
    
    target = re.sub(r'[,.\/?!-=]'," ",target.lower()).split()

    return target
    

def get_lemms(target=None):
    """
        lemmatizes array of strings

        returns an array of lemms
    """

    lemmer = WordNetLemmatizer()

    return list(map(lambda x: lemmer.lemmatize(x),target))


def remove_stopwords(target=None,stop_words=None):
    """
        removes a given set of stopwords
    """
    if stop_words is None:
        stop_words = set(nltk_stopwords.words('english'))

    return [x for x in target if x not in stop_words]

def get_word_freq(target=None,least_common=1000):
    fd = nltk.FreqDist(target)
    fd = list(fd)[-least_common:]
    return fd

def get_most_common(target=None,number=2000):
    freq = nltk.FreqDist(target)
    return list(freq)[:number]

def apply_nlp_treatment(df=None,text_col=None,words=1000):
    if df is None or text_col is None:
        return None

    # get tokens of all words
    tokens = get_tokens(target=df[text_col])

    # remove stop words
    tokens_no_stop = remove_stopwords(target=tokens)

    # least common words
    freq = get_word_freq(target=tokens_no_stop,least_common=2000)


def most_common_words(target=None):
    """
        gets the most common words and builds the independant variables
    """

    # get tokens
    tokens = get_tokens(target=target)

    # filter out stop words
    filtered_tokens = remove_stopwords(target=tokens)

    # get lemms
    lemms = get_lemms(target=filtered_tokens)

    # take the N most common words
    most_common = get_most_common(target=lemms,number=2000)

    df = {}
    for word in most_common:
        df[f"x_{word}"] = target.apply(lambda x: 1 if word in x else 0)

    df = pd.DataFrame(df)

    return df
        


    
