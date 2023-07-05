import numpy as np
import pandas as pd

from Reader.DataReader import DataReader
from learning.DataCleaner import DataCleaner
from learning.DataSplitter import DataSplitter
from logisticRegression.LogisticRegression import LogisticRegression
from models.PredictRequest import PredictRequest


class Learn:

    def __init__(
            self,
            reader: DataReader,
            data_cleaner: DataCleaner,
            data_splitter: DataSplitter,
            logistic_regression: LogisticRegression
    ):
        self.reader = reader
        self.data_cleaner = data_cleaner
        self.data_splitter = data_splitter
        self.model = logistic_regression

    def learn(self):
        x_train, x_test, y_train, y_test = self.data_splitter.train_test_split(self.reader.get_X(), self.reader.get_y())

        x_train, x_test = self.data_cleaner.standardize_data(X_train=x_train, X_test=x_test)

        self.model.fit(x_train, y_train)

        y_pred = self.model.predict(x_test)
        accuracy = np.sum(y_pred == y_test) / len(y_test)

        return {
            "accuracy": accuracy
        }

    def set_reader(self, new_reader: DataReader):
        self.reader = new_reader

    def get_reader(self):
        return self.reader

    def predict(self, data: PredictRequest):

        data = {
            "Pregnancies": [data.pregnancies],
            "Glucose": [data.glucose],
            "BloodPressure": [data.bloodPressure],
            "SkinThickness": [data.skinThickness],
            "Insulin": [data.insulin],
            "BMI": [data.BMI],
            "DiabetesPedigreeFunction": [data.diabetesPedigreeFunction],
            "Age": [data.age]
        }

        df = pd.DataFrame(data)
        df = self.data_cleaner.transform(df)

        y_pred = self.model.predict(df)

        message = "Diabetic" if y_pred[0] else "Non-Diabetic"
        return {
            "message": message
        }
