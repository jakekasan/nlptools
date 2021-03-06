"""
    TF-IDF

    should take a pd.Series of raw text
"""

from approaches.bow import BagOfWords
import math

class TFIDF(BagOfWords):
    def __init__(self,name=None,limit=None):
        self.name = name or "Tf-Idf"
        BagOfWords.__init__(self,name=self.name)
        self.bags = None
        self.prototype = None
        self.documents = None
        self.totalBag = None
        self.limit = limit or None
        pass

    def info(self):
        print(self.__str__())

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

        n = len(self.bags)

        filtered_prototype = {}
        # remove words which appear in every document (thus guarenteeing a zero)
        for key in prototype.keys():
            if prototype[key] < n:
                filtered_prototype[key] = prototype[key]

        # def idf_not_zero(item):
        #     for bag in self.bags:
        #         if item[0] not in bag.keys():
        #             return True
        #     return False

        prototype = filtered_prototype

        prototype = [x for x in sorted(prototype.items(),key=lambda x: x[1])]

        # now filter out words with an idf of 0...

        if self.limit is not None:
            prototype = prototype[:self.limit]

        prototype = {a:b for a,b in prototype}

        self.totalBag = prototype
        self.prototype = sorted(prototype.keys())

    def apply(self,document):
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
        return self.get_word_tf(word,document_bag) * self.get_word_idf(word)

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
        
    def __str__(self):
        return f"\nName: {self.name}\nBuild: {self.prototype is not None}\nArray Length: {len(self.prototype)}\n"
        

    

        
