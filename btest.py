import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("./rbs_processed.csv")

count = 0

print("labels" in df.columns)

vals = df.drop("labels",axis=1)

# check if any row is empty
#count = sum(0 == vals.apply(lambda x: sum(x.apply(lambda x: (x != 0))), axis=1))

x_train, x_test, y_train, y_test = train_test_split(vals,df["labels"],test_size=0.4)

#knn = KNeighborsClassifier(n_neighbors=5)
#dt = DecisionTreeClassifier(criterion="gini")
rf = RandomForestClassifier()

cv_results = cross_validate(rf,x_train,y_train,cv=10)

print(cv_results)

# print("Model fit")

# knn.fit(x_train,y_train)

# print(knn.score(x_test,y_test))

# sample = df.sample(20)

# print("Sample selected")
# print("Labels:",sample["labels"])

# targets = sample["labels"]
# preds = knn.predict(sample.drop("labels",axis=1))

# print("Actu.\tPred")
# for act,pred in zip(targets,preds):
#     print(f"{act}\t{pred}")

