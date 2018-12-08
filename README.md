# Sallie Mae Mortgage Loans

For this project, we will be working with Sallie Mae's mortgage loan data. The goal is to predict whether a mortgage loan will be forclosed in the future. This is a classification problem with the target variable is either a yes or a no.

The data can be [downloaded here](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html). The files used were from 2015 Q1 performance and acquisition tables.

The data was prepared using postgreSQL before it was imported into python. The code used is called "SQL query", and you can find it in this folder.

The prepared data that you can import into Python consits of 2 files called performance.csv and acquisition.csv. 

The Python file to run is called "Sallie Mae.py".

The training/ test data was split 80%/ 20% and the accuracy for the model came out to be 92% using simple logistic regression.
