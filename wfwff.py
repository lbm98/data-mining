import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.base import BaseEstimator, TransformerMixin

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    df = pd.read_excel('data/existing-customers.xlsx')


class UniformImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.freqs_ = X.value_counts(normalize=True)
        return self

    def transform(self, X, y=None):
        X = X.copy()
        missing = X.isna()
        n_missing = missing.sum()
        fill_values = pd.Series(np.random.choice(self.freqs_.index, size=n_missing, p=self.freqs_.values))
        X[missing] = fill_values.values
        return X