"""
    class from which approaches inherit
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

import unittest

class Approach:
    def __init__(self,name=None,corpus=None):
        self.name = name or "Untitled"
        self.corpus = corpus

    def buildApproach(self,df=None):
        """
            takes 
        """
        if df is None:
            raise

    def processRaw(self,raw):
        """
            once approach is built, this function can be used for getting inputs from raw text
        """

        tokens = word_tokenize(raw)
        pos = pos_tag(tokens)
        lemms = self.lemmatizeDocument(pos)

        return lemms


    def tokenize(self,data):
        """
            returns list of tuples with tokens + POS
        """
        
        # tokens
        documents = list(map(lambda x: word_tokenize(x),data))

        # pos
        documents = list(map(lambda x: pos_tag(x),documents))

        return documents

    def lemmatizeDocument(self,tokens):
        """
            returns lemms for single document
        """

        lemmer = WordNetLemmatizer()

        lemms = [lemmer(a,pos=b) for a,b in tokens]

    def lemmatizeCorpus(self,corpus):
        """
            returns lemms for entire corpus
        """
        lemms = list(map(lambda x: self.lemmatizeDocument(x),corpus))
        return lemms

class TestApproach(unittest.TestCase):
    def setUp(self):
        self.app = Approach()

    def test_init(self):
        self.assertIsInstance(self.app,Approach)

    def test_init()

def main():
    unittest.main()

if __name__ == '__main__':
    main()