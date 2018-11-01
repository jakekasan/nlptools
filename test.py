from approaches.tfidf import TFIDF

import pandas as pd

# data_dir = "./../stock-sentiment/test.csv"

# df = pd.read_csv(data_dir)


# train = df.sample(10)["text"].values
# test = df.sample(2)["text"].values

# print(df.shape)

# tf = TFIDF()

# #corpus = df["text"].values

# #print(corpus)

# print("Building...")

# tf.build(corpus=train)

# print("Approach built!")

# #print(tf.prototype)

# results = list(map(lambda x: tf.apply(x),test))

# for row in results:
#     print(row)

# res_dict = {}
# for i,word in enumerate(tf.prototype):
#     res_dict[word] = [x[i] for x in results]



# results_df = pd.DataFrame(res_dict)

# results_df.to_csv("./results.csv")

#print(list(filter(lambda x: x > 0.0,results)))

#tf.build(corpus=)


from nltk.corpus import movie_reviews

def remove_bad(string):
    string = string.replace("\n","")
    string = string.replace("\'","'")
    return string

documents = [(remove_bad(movie_reviews.raw(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

documents = documents[:200] + documents[-200:]

corpus = [a for a,b in documents]
labels = [b for a,b in documents]

tf = TFIDF()


print("Building...")

tf.build(corpus=corpus)

print("Approach built!")

print(f"Length of prototype: {len(tf.prototype)}")

#results = list(map(lambda x: tf.apply(x),corpus))

import multiprocessing.pool

pool = multiprocessing.pool.ThreadPool(processes=500)

results = pool.map(tf.apply,corpus)

print("Finished working on test set")

res_dict = {}
for i,word in enumerate(tf.prototype):
    res_dict[word] = [x[i] for x in results]

res_dict["labels"] = labels

results_df = pd.DataFrame(res_dict)

results_df.to_csv("./movie_reviews.csv")

print("done!")