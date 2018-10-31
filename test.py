from approaches.tfidf import TFIDF

import pandas as pd

data_dir = "./../stock-sentiment/test.csv"

df = pd.read_csv(data_dir).head(2)

print(df.head())


tf = TFIDF()

corpus = df["text"].values

#print(corpus)

corpus = ["What is this?","This is it"]

tf.build(corpus=corpus)

print("Done!")

print(tf)

print(tf.apply("What is up, big chief?"))

#tf.build(corpus=)