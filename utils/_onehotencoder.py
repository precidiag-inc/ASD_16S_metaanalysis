import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin

class OneHotEncoder(TransformerMixin):
    def __init__(self, covariates):
        self.covariates = covariates
        self.transformed_covariates = []

    def fit(self, df, *args, **kwargs):
        from sklearn.preprocessing import OneHotEncoder
        self.encoder = OneHotEncoder()
        self.dummies = self.encoder.fit_transform(df[self.covariates]).toarray()

        return self

    def transform(self, df, *args, **kwargs):
        temp = df.copy()
        temp.drop(self.covariates, axis=1, inplace=True)

        columns = np.array([])
        for i, covariate in enumerate(self.covariates):
            columns = np.append(columns, covariate + '_' + self.encoder.categories_[i])

        self.dummies = pd.DataFrame(self.dummies, columns=columns, index=df.index)
        self.transformed_covariates = list(columns)

        return pd.concat([temp, self.dummies], axis=1)