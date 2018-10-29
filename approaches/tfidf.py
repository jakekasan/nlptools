"""
    TF-IDF

    should take a pd.Series of raw text
"""

from approaches.bow import BagOfWords
import math

class TFIDF(BagOfWords):
    def __init__(self,data=None):
        BagOfWords.__init__(self,data=data)
        self.bags = None
        self.prototype = None
        self.documents = None
        self.bags = None
        self.totalBag = None
        self.limit = None
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

        # get bag
        bag = self.get_bag_from_document(document)

        return [self.get_tf_idf(x,bag) for x in self.prototype]
    

    def get_tf_idf(self,word,document_bag):
        """
            returns 
        """
        return self.get_word_tf * self.get_word_idf

    def get_word_idf(self,word):
        """
            returns the inverse document frequency

            formula:
                log(number of document/ number of documents with term)
        """
        number_of_documents = len(self.bags)
        number_of_documents_with_term = 0
        for document in self.bags:
            if word in document.keys():
                number_of_documents_with_term += 1

        return math.log((number_of_documents/number_of_documents_with_term),2)

    def get_word_tf(self,word,document_bag):
        """
            returns a term frequency (between 0 and 1)
        """
        all_words = sum(document_bag.values())
        word_count = 0
        if word in document_bag.keys():
            word_count = document_bag[word]
            
        return word_count / all_words
        
        

    

        
