"""
    Bag Of Words
"""
from approach import Approach
import unittest

class BagOfWords(Approach):
    def __init__(self,corpus=None,limit=None):
        Approach.__init__(self,name="Bag Of Words",corpus=corpus)
        self.rawData = corpus
        self.documents = None
        self.bags = None
        self.totalBag = None
        self.result = None
        self.limit = limit
        self.prototype = None
        pass

    def build(self,corpus=None):
        """
            builds a Bag-Of-Words approach given some corpus
            once it is built, the class can be used to transform further
            raw text into a numerical form.
        """
        documents = self.tokenize(self.rawData)
        self.documents = self.lemmatizeDocument(documents)

        self.bags = list(map(lambda x: individualBags(x),self.documents))

        prototype = {}
        for bag in self.bags:
            for word,count in bag.items():
                if word in prototype.keys():
                    prototype[word] += 1
                else:
                    prototype[word] = 1

        prototype = [x for x in sorted(prototype.items(),key=lambda x: x[1])]

        if self.limit is not None:
            prototype = prototype[:self.limit]

        prototype = {a:b for a,b in prototype}

        self.totalBag = prototype
        self.prototype = prototype.keys()

    def variablesFromRaw(self,raw):
        """
            returns an array of variables for a given array
        """
        document = self.processRaw(raw)
        bag = self.individualBags(document)

        return [bag[x] if x in bag.keys() else 0 for x in self.prototype]

    def individualBags(self,tokens):
        """
            takes a tokens of a document
            returns a dictionary of bag of words
        """
        bag = {}
        for word in tokens:
            if word in bag.keys():
                bag[word] += 1
            else:
                bag[word] = 1
        return bag


class BOWTest(unittest.TestCase):

    def setUp(self):
        self.bow = BagOfWords()

    def test_class(self):
        self.assertIsInstance(self.bow,BagOfWords)

    def test_individualBags(self):
        """
            A comment!
        """
        string = ["Heavy", "hangs", "the", "head"]
        desired = {"Heavy":1,"hangs":1,"the":1,"head":1}
        actual = self.bow.individualBags(string)
        self.assertEqual(desired,actual)

    

def main():
    unittest.main()

if __name__ == '__main__':
    main()

    
