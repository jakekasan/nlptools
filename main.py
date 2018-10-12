import re
import nltk

from nltk.corpus import stopwords as nltk_stopwords
from nltk.stem import WordNetLemmatizer

def get_tokens(target=None):
    """
        takes a string or array and returns an array of all words, lowercase 
    """
    if target is None:
        return []
    
    target = re.sub(r'/W'," ",target).split()

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


    
