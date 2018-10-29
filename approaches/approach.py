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

    def process_document(self,document,pos=False):
        """
            once approach is built, this function can be used for getting inputs from raw text
        """

        tokens = self.tokenize_document(document,pos=pos)
        lemms = self.lemmatize_document(tokens)

        return lemms

    def tokenize_document(self,document,pos=False):
        """
            returns a list of tuples with POS
        """
        tokens = word_tokenize(document)
        #tokens = list(map(lambda x: x.lower(),tokens))
        tokens = [w.lower() for w in tokens]
        tokens_pos = pos_tag(tokens)
        if pos:
            return tokens_pos
        return tokens


    def tokenize_corpus(self,corpus,pos=False):
        """
            returns list of tuples with tokens + POS
        """
        
        return [self.tokenize_document(x,pos=pos) for x in corpus]
        #list(map(lambda x: self.tokenize_document(x,pos=pos),corpus))


    def lemmatize_document(self,document):
        """
            returns lemms for single document
        """

        lemmer = WordNetLemmatizer()

        lemms = [lemmer(a,pos=b) for a,b in document]

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

    def test_tokenize(self):
        string = "Hello world"
        expected = ["hello","world"]
        actual = self.app.tokenize_document(string,pos=False)
        self.assertEqual(expected,actual)

    def test_pos(self):
        string = "Hello world"
        expected = [("hello","NN"),("world","NN")]
        actual = self.app.tokenize_document(string,pos=True)
        self.assertEqual(expected,actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()