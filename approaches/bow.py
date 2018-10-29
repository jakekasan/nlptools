"""
    Bag Of Words
"""
from approaches.approach import Approach

class BagOfWords(Approach):
    def __init__(self,corpus=None,limit=None):
        Approach.__init__(name="Bag Of Words",corpus=corpus)
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

        prototype = [x for x in sorted(prototype.items(),key=lambda (k,v): (v,k))]

        if self.limit not None:
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

        return [bag[x] if x in bag.keys() for x in self.prototype]

    def individualBags(self,document):
        bag = {}
        for word in document:
            if word in bag.keys():
                bag[word] += 1
            else:
                bag[word] = 1
        return bag
