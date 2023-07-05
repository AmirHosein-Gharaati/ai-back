from fastapi import FastAPI

from Reader.Reader import Reader
from learning.DataCleaner import DataCleaner
from learning.DataSplitter import DataSplitter
from learning.Learn import Learn
from logisticRegression.LogisticRegression import LogisticRegression

app = FastAPI()


@app.get("/")
async def root():
    reader = Reader('data/diabetes2.csv', 'Outcome')
    data_splitter = DataSplitter(reader, test_size=0.2, random_state=0)

    data_cleaner = DataCleaner()
    logistic_regression = LogisticRegression()

    learner = Learn(data_cleaner, data_splitter, logistic_regression)
    learner.learn()
