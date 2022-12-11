import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class Model1API:
    def __init__(self, filePath, independentVars, dependentVar):
        self.df = pd.read_csv(filePath)
        self.df = pd.get_dummies(self.df, drop_first=True)
        xIndices = [self.df.columns.get_loc(c) for c in independentVars if c in self.df]
        yIndex = self.df.columns.get_loc(dependentVar)

        X = self.df.iloc[:,xIndices]
        y = self.df.iloc[:,yIndex]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        self.LM_pred = None
        self.LM = None

    def predict(self, data):
        self.LM_pred = self.LM.predict(data)
        return self.LM_pred

    def train(self):
        self.LM = LinearRegression()
        self.LM.fit(self.X_train, self.y_train)

    def performance(self):
        self.predict(self.X_test)
        print('MAE:', metrics.mean_absolute_error(self.y_test, self.LM_pred))
        print('MSE:', metrics.mean_squared_error(self.y_test, self.LM_pred))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(self.y_test, self.LM_pred)))


if __name__ == "__main__":
    # for testing
    Linear_Model = ModelAPI("car_web_dataset.csv", ["Year", "Present_Price", "Kms_Driven", "Fuel_Type_Diesel", "Fuel_Type_Petrol", "Seller_Type_Individual", "Transmission_Manual"], "Selling_Price")
    Linear_Model.train()
    Linear_Model.performance()




