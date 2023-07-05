import numpy as np

from learning.DataCleaner import DataCleaner
from learning.DataSplitter import DataSplitter
from logisticRegression.LogisticRegression import LogisticRegression


class Learn:

    def __init__(
            self,
            data_cleaner: DataCleaner,
            data_splitter: DataSplitter,
            logistic_regression: LogisticRegression
    ):
        self.data_cleaner = data_cleaner
        self.data_splitter = data_splitter
        self.model = logistic_regression

    def learn(self):
        x_train, x_test, y_train, y_test = self.data_splitter.train_test_split()

        x_train = self.data_cleaner.fit_transform(x_train)
        x_test = self.data_cleaner.transform(x_test)

        self.model.fit(x_train, y_train)
        y_pred = self.model.predict(x_test)
        accuracy = np.sum(y_pred == y_test) / len(y_test)
        print('Accuracy:', accuracy)