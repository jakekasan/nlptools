"""
    TF-IDF

    should take a pd.Series of raw text
"""

class TFIDF(Approach):
    def __init__(self,data=None):
        self.rawData = data
        self.documents = None
        pass

    def build(self):
        documents = self.tokenize(self.rawData)
        self.documents = self.lemmatizeDocument(documents)
        pass

    

        
