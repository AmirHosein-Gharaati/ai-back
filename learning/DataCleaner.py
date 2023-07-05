from sklearn.preprocessing import StandardScaler


class DataCleaner:

    def __init__(self):
        self.scaler = StandardScaler()

    def standardize_data(self, X_train, X_test):
        x_train = self.fit_transform(X_train)
        x_test = self.transform(X_test)

        return x_train, x_test

    def fit_transform(self, X_train):
        return self.scaler.fit_transform(X_train)

    def transform(self, X_test):
        return self.scaler.transform(X_test)
