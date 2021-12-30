import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.linear_model import LogisticRegression
import os
from sklearn.preprocessing import StandardScaler

# covariates: must be numerical, exact matches can be anything, treatment_group must be dict
# if covariates is None, use everything


class PropensityScore(TransformerMixin):
    def __init__(self, treatment_group: dict, covariates: list = [], exact: list = [], repeat:bool = True, model = LogisticRegression()):
        assert isinstance(treatment_group, dict), "Error: treatment_group must be a dictionary {column: value}"
        assert len(treatment_group) == 1, "Error: treatment_group must be length 1"
        self.treatment_group_column = list(treatment_group.keys())[0]
        self.treatment_group_value = list(treatment_group.values())[0]
        self.covariates = covariates
        self.exact = exact
        self.repeat = repeat
        self.all_variables = covariates + exact
        self.model = model

    def fit(self, df, *args, **kwargs):
        assert all([variable in df for variable in self.all_variables]), "Error: some variables are not found in dataframe"
        assert df[self.covariates].apply(lambda s: pd.to_numeric(s, errors = 'coerce').notnull().all()).all(), "Error: some covariates are not numerical"
        assert self.treatment_group_value in df[self.treatment_group_column].unique(), "Error: treatment_group values not in dataframe column"
        assert df[self.treatment_group_column].unique().size == 2, "Error: treatment_group column must only have two types of unique values"

        self.dataframe = df.copy()

        x = self.dataframe.loc[:, self.covariates]
        y = self.dataframe.loc[:, self.treatment_group_column]

        x = StandardScaler().fit_transform(x)
        self.model.fit(x, y)
        self.dataframe['propensity_scores_'] = self.model.predict_proba(x)[:, 0]
        return self

    def transform(self, df, *args, **kwargs):
        assert hasattr(self, 'dataframe'), "Error: please run fit before transform"

        _treatment = self.dataframe[self.dataframe[self.treatment_group_column] == self.treatment_group_value].copy()
        _control = self.dataframe[self.dataframe[self.treatment_group_column] != self.treatment_group_value].copy()
        self.dropped = []

        control = pd.DataFrame()
        for i, features in _treatment.iterrows():
            if self.exact:
                subset = _control[(_control[self.exact] == features[self.exact]).all(axis = 1).values]
            else:
                subset = _control
            if subset.empty:
                self.dropped.append(i)
                continue

            indices = np.abs(features['propensity_scores_'] - subset['propensity_scores_']).sort_values()
            
            if self.repeat:
                temp = [subset.loc[index] for index in indices.index] 
            else:    
                temp = [subset.loc[index] for index in indices.index if index not in control.index]
            
            if len(temp) == 0:
                self.dropped.append(i)
            else:
                control = control.append(temp[0])
            

        _treatment.drop(index = self.dropped, inplace = True)
        self._treatment = _treatment.copy()
        print(f'{len(self.dropped)} entries dropped.')

        df = pd.concat([_treatment, control])
        df.drop('propensity_scores_', axis = 1, inplace = True)
        return df