"""
    Bag Of Words
"""
from approaches.approach import Approach

class BagOfWords(Approach):
    def __init__(self,data,limit=None):
        self.rawData = data
        self.documents = None
        self.bags = None
        self.bagPrototype = None
        self.result = None
        self.limit = limit
        pass

    def build(self):
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

        self.bagPrototype = prototype
        
    def individualBags(self,document):
        bag = {}
        for word in document:
            if word in bag.keys():
                bag[word] += 1
            else:
                bag[word] = 1
        return bag

    def (self):
        for
            