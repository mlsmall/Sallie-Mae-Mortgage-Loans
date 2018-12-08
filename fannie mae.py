# Fannie Mae Mortgage Loans
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the files into Python and joining them
acquisition = pd.read_csv('acquisition.csv')
performance = pd.read_csv('performance.csv')

dataset=pd.merge(acquisition, performance, on='id', how='inner')

# Encoding the Dataset
from sklearn.preprocessing import LabelEncoder
dataset=dataset.apply(LabelEncoder().fit_transform)

# Filling missing values with 0
dataset = dataset.fillna(0)

dataset["foreclosure_date"].value_counts()

# Defining X and y
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 25]

# Splitting the data into a training set and a test set
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2)

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

# Generating prediction model with balanced class weight and training data
model = LogisticRegression(class_weight="balanced", solver="liblinear", multi_class = 'ovr')
model.fit(Xtrain,ytrain)

# Generating predictions with the testing data
predictions = model.predict(Xtest)

# Computing the model accuracy
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(ytest, predictions)

accuracy = accuracy_score(ytest, predictions)
