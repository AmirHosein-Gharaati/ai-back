from sklearn.model_selection import train_test_split

from Reader.Reader import Reader


class DataSplitter:

    def __init__(self, reader: Reader, test_size: float, random_state: int):
        self.X = reader.get_X()
        self.y = reader.get_y()
        self.test_size = test_size
        self.random_state = random_state

    def train_test_split(self):
        return train_test_split(self.X, self.y, test_size=self.test_size, random_state=self.random_state)

    def set_X_and_y(self, reader: Reader):
        self.X = reader.get_X()
        self.y = reader.get_y()
