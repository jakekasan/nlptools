"""
    Bag Of Words
"""
from approaches.approach import Approach
import unittest

class BagOfWords(Approach):
    def __init__(self,name=None,limit=None):
        self.name = name or "Bag of Words"
        Approach.__init__(self,name=self.name)
        #self.rawData = corpus
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
        documents = self.tokenize_corpus(corpus,pos=True)
        self.documents = self.lemmatize_corpus(documents)

        self.bags = [self.individual_bags(x) for x in self.documents]

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
        self.prototype = sorted(prototype.keys())

    def variablesFromRaw(self,raw):
        """
            returns an array of variables for a given array
        """
        document = self.process_document(raw,pos=True)
        bag = self.individual_bags(document)

        return [bag[x] if x in bag.keys() else 0 for x in self.prototype]

    def individual_bags(self,tokens):
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

    def get_bag_from_document(self,document):
        """
            processes raw text and returns a bag
        """

        tokens = self.process_document(document,pos=True)
        bag = self.individual_bags(tokens)

        return bag


sample_corpus = ["This is a sentence","This is another sentence","And here is a phrase"]
corpus_bow = {
    "this":2,
    "is":3,
    "a":2,
    "sentence":2,
    "another":1,
    "and":1,
    "here":1,
    "phrase":1
}

test_text = "This is a sentence"
test_result = [1 if y in [x.lower() for x in test_text.split(" ")] else 0 for y in sorted(corpus_bow.keys())]



class BOWTest(unittest.TestCase):

    def setUp(self):
        self.bow = BagOfWords()

    def test_class(self):
        self.assertIsInstance(self.bow,BagOfWords)

    def test_individual_bags(self):
        """
            A comment!
        """
        string = ["Heavy", "hangs", "the", "head"]
        desired = {"Heavy":1,"hangs":1,"the":1,"head":1}
        actual = self.bow.individual_bags(string)
        self.assertEqual(desired,actual)

    def test_build(self):
        print(sample_corpus)
        self.bow.build(corpus=sample_corpus)

        actual = self.bow.variablesFromRaw(test_text)
        desired = [[1, 0, 0, 0, 1, 0, 1, 1]]

        self.assertEqual(actual,desired)



    



    

    

def main():
    unittest.main()

if __name__ == '__main__':
    main()

    
