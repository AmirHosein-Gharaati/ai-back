from pandas import DataFrame
from sklearn.model_selection import train_test_split


class DataSplitter:

    def __init__(self, test_size: float, random_state: int):
        self.test_size = test_size
        self.random_state = random_state

    def train_test_split(self, X: DataFrame, y: DataFrame):
        return train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)