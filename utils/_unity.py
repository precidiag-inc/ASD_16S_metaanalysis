import numpy as np
from sklearn.base import TransformerMixin
import pandas as pd

class UnityScaler(TransformerMixin):
    def __init__(self, axis = 1):
        assert (axis == 1) or (axis == 0), "Error: axis must be either 0 or 1"
        self.axis = axis
        
    def fit(self, df, *args, **kwargs):
        return self
    def transform(self, df, *args, **kwargs):
        df = df.copy()
        if self.axis == 1:
            df /= np.sum(df, axis = self.axis)[:, None]
        elif self.axis == 0:
            df /= np.sum(df, axis = self.axis)
        return df.fillna(0)
