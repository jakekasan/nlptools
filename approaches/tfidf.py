"""
    TF-IDF

    should take a pd.Series of raw text
"""

from approaches.bow import BagOfWords

class TFIDF(BagOfWords):
    def __init__(self,data=None):
        BagOfWords.__init__(self,data=data)
        self.bags = None
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

    def process_document(self,document):
        """
            returns a list of td-idf values
        """

    def get_tf_idf(self,word,bags):
        """
            returns 
        """

    def get_word_idf(self,word):
        """
            returns the inverse document frequency

            formula:
                log()
        """
        pass

    def get_word_tf(self,word,document):
        """
            returns a term frequency (between 0 and 1)
        """
        pass
        

    

        
