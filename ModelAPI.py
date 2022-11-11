import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class ModelAPI:
    def __init__(self, filePath, independentVars, dependentVar):
        self.df = pd.read_csv(filePath)
        self.df = pd.get_dummies(df, drop_first=True)
        xIndices = [self.df.columns.get_loc(c) for c in independentVars if c in self.df]
        yIndex = self.df.columns.get_loc(dependentVar)

        x = self.df.iloc[xIndices]
        y = self.df.iloc[yIndex]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        self.LM_pred = None
        self.LM = None

    def predict(self, data):
        self.LM_pred = self.LM.predict(data)
        return self.LM_pred

    def train(self, data):
        self.LM = LinearRegression()
        self.LM.fit(self.X_train, self.y_train)

    def performance(self, data):
        self.LM_pred = LM.predict(data)
        print('MAE:', metrics.mean_absolute_error(self.y_test, self.LM_pred))
        print('MSE:', metrics.mean_squared_error(self.y_test, self.LM_pred))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(self.y_test, self.LM_pred)))







