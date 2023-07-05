import pandas as pd


class Reader:

    def __init__(self, filepath: str, result_label: str):
        self.dataframe = pd.read_csv(filepath)
        self.result_label = result_label

        self.X = self.dataframe.drop(self.result_label, axis=1)
        self.y = self.dataframe[self.result_label]

    def get_X(self):
        return self.X

    def get_y(self):
        return self.y
