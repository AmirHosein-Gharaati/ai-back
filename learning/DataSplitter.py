from sklearn.model_selection import train_test_split


class DataSplitter:

    def __init__(self, X, y, test_size: float, random_state: int):
        self.X = X
        self.y = y
        self.test_size = test_size
        self.random_state = random_state

    def train_test_split(self):
        return train_test_split(self.X, self.y, self.test_size, self.random_state)
