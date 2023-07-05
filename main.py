from fastapi import FastAPI

from Reader.DataReader import DataReader
from learning.DataCleaner import DataCleaner
from learning.DataSplitter import DataSplitter
from learning.Learn import Learn
from logisticRegression.LogisticRegression import LogisticRegression

app = FastAPI()

learner = Learn(
    reader=DataReader('data/diabetes2.csv', 'Outcome'),
    data_cleaner=DataCleaner(),
    data_splitter=DataSplitter(test_size=0.2, random_state=0),
    logistic_regression=LogisticRegression()
)

learner.learn()

@app.get("/")
async def root():
    return "Hello World"
