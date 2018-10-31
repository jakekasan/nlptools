"""
    class from which approaches inherit
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

import re
import unittest

class Approach:
    def __init__(self,name=None,corpus=None):
        self.name = name or "Untitled"
        self.corpus = corpus
        self.lemmer = WordNetLemmatizer()

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
        #tokens = word_tokenize(document)
        #tokens = list(map(lambda x: x.lower(),tokens))
        tokens = re.split(r" |[\.\,\?\!\'\"\\\/\(\)\[\]]",document)
        tokens = [w.lower() for w in tokens if w != ""]
        if not pos:
            return tokens
        tokens_pos = pos_tag(tokens)
        tokens_pos = [(a,self.get_wordnet_tag(b)) for a,b in tokens_pos]
        return tokens_pos
        


    def tokenize_corpus(self,corpus,pos=False):
        """
            returns list of tuples with tokens + POS
        """
        
        return [self.tokenize_document(x,pos=pos) for x in corpus]
        #list(map(lambda x: self.tokenize_document(x,pos=pos),corpus))


    def lemmatize_document(self,tokens):
        """
            returns lemms for single document
        """
        try:
            return [self.lemmer.lemmatize(a,self.get_wordnet_tag(b)) for a,b in tokens]
        except:
            print(tokens)
            raise ValueError


    def lemmatize_corpus(self,corpus):
        """
            returns lemms for entire corpus
        """
        #lemms = list(map(lambda x: self.lemmatize_document(x),corpus))
        return [self.lemmatize_document(x) for x in corpus]

    def get_wordnet_tag(self,tag):
        """
            return wordnet tag for corresponding treebank tag
        """
        tag_map = {
        'CC':None, # coordin. conjunction (and, but, or)  
        'CD':wn.NOUN, # cardinal number (one, two)             
        'DT':None, # determiner (a, the)                    
        'EX':wn.ADV, # existential ‘there’ (there)           
        'FW':None, # foreign word (mea culpa)             
        'IN':wn.ADV, # preposition/sub-conj (of, in, by)   
        'JJ':[wn.ADJ, wn.ADJ_SAT], # adjective (yellow)                  
        'JJR':[wn.ADJ, wn.ADJ_SAT], # adj., comparative (bigger)          
        'JJS':[wn.ADJ, wn.ADJ_SAT], # adj., superlative (wildest)           
        'LS':None, # list item marker (1, 2, One)          
        'MD':None, # modal (can, should)                    
        'NN':wn.NOUN, # noun, sing. or mass (llama)          
        'NNS':wn.NOUN, # noun, plural (llamas)                  
        'NNP':wn.NOUN, # proper noun, sing. (IBM)              
        'NNPS':wn.NOUN, # proper noun, plural (Carolinas)
        'PDT':[wn.ADJ, wn.ADJ_SAT], # predeterminer (all, both)            
        'POS':None, # possessive ending (’s )               
        'PRP':None, # personal pronoun (I, you, he)     
        'PRP$':None, # possessive pronoun (your, one’s)    
        'RB':wn.ADV, # adverb (quickly, never)            
        'RBR':wn.ADV, # adverb, comparative (faster)        
        'RBS':wn.ADV, # adverb, superlative (fastest)     
        'RP':[wn.ADJ, wn.ADJ_SAT], # particle (up, off)
        'SYM':None, # symbol (+,%, &)
        'TO':None, # “to” (to)
        'UH':None, # interjection (ah, oops)
        'VB':wn.VERB, # verb base form (eat)
        'VBD':wn.VERB, # verb past tense (ate)
        'VBG':wn.VERB, # verb gerund (eating)
        'VBN':wn.VERB, # verb past participle (eaten)
        'VBP':wn.VERB, # verb non-3sg pres (eat)
        'VBZ':wn.VERB, # verb 3sg pres (eats)
        'WDT':None, # wh-determiner (which, that)
        'WP':None, # wh-pronoun (what, who)
        'WP$':None, # possessive (wh- whose)
        'WRB':None, # wh-adverb (how, where)
        '$':None, #  dollar sign ($)
        '#':None, # pound sign (#)
        '“':None, # left quote (‘ or “)
        '”':None, # right quote (’ or ”)
        '(':None, # left parenthesis ([, (, {, <)
        ')':None, # right parenthesis (], ), }, >)
        ',':None, # comma (,)
        '.':None, # sentence-final punc (. ! ?)
        ':':None # mid-sentence punc (: ; ... – -)
        }

        if type(tag) == str and tag in [x for x in tag_map.values() if x is not None]:
            return tag

        if (type(tag) != str) or (tag not in tag_map.keys()):
            return wn.NOUN
            
        for key,value in tag_map.items():
            if value is None:
                tag_map[key] = wn.NOUN

        to_return = tag_map[tag]

        if to_return is None:
            to_return = wn.NOUN

        return to_return





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
        expected = [("hello",wn.NOUN),("world",wn.NOUN)]
        actual = self.app.tokenize_document(string,pos=True)
        self.assertEqual(expected,actual)

    def test_wordnet_tagger_alreadytagged(self):
        expected = wn.NOUN
        self.assertEqual(expected,self.app.get_wordnet_tag(expected))

    def test_wordnet_tagger_not_tagged_legit(self):
        expected = wn.NOUN
        self.assertEqual(expected,self.app.get_wordnet_tag("NN"))

    def test_wordnet_tagger_not_tagged_nonlegit(self):
        expected = wn.NOUN
        self.assertEqual(expected,self.app.get_wordnet_tag("this is crap"))

def main():
    unittest.main()

if __name__ == '__main__':
    main()