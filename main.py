from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from reader.DataReader import DataReader
from learning.DataCleaner import DataCleaner
from learning.DataSplitter import DataSplitter
from learning.Learn import Learn
from logisticRegression.LogisticRegression import LogisticRegression
from models.PredictRequest import PredictRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post("/predict")
async def predict(predictRequest: PredictRequest):
    return learner.predict(predictRequest)


@app.post("/dataset/{dataset_number}")
async def select_dataset(dataset_number: int):

    if dataset_number == 1:
        data_reader = DataReader('data/diabetes1.csv', 'Outcome')
    elif dataset_number == 2:
        data_reader = DataReader('data/diabetes2.csv', 'Outcome')
    else:
        return HTTPException(status_code=400, detail="Bad value")

    learner.set_reader(data_reader)
    return learner.learn()
