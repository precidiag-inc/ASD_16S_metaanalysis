import pandas as pd
from sklearn.base import TransformerMixin
import numpy as np

taxa = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species', 'none']

class CollapseTaxaTransformer(TransformerMixin):
    def __init__(self, level=None, aggregation='sum'):
        self.level = level
        self.aggregation = aggregation

    def fit(self, x, *args, **kwargs):
        return self

    def transform(self, df, *args, **kwargs):
        df = df.copy()

        if self.level == None or self.level == 'None':
            return df

        taxa_header_index = taxa.index(self.level)  # the index of the level
        
        df.columns = [' '.join(row) for row in df.T.index.to_frame().iloc[:, :taxa_header_index + 1].replace(np.nan, 'nan').values]
        
        return df.groupby(df.columns, axis = 1).sum()
        
        
        """
        index = pd.MultiIndex.from_frame(
            df.T.index.to_frame().iloc[:, :taxa_header_index + 1])  # subset the multi-index to the right level
        df.columns = [m for m in index]  # aggregate multi-index to a tuple
        df.columns.name = '_'  # temporarily call the columns '_'

        x = []
        for name, group in df.T.groupby('_'):  # group by '_' and aggregate similar columns
            group_ = group.agg(self.aggregation)  # aggregate using the "function"
            group_.name = pd.MultiIndex.from_tuples(group.index)[0][taxa_header_index]  # set new multi-index
            x.append(group_)  # add to the list
        df = pd.DataFrame(x).T  # convert to dataframe
        df = df.groupby(lambda x: x, axis=1).agg(self.aggregation)
        df.columns.names = taxa[taxa_header_index:taxa_header_index + 1]  # rename columns
        return df
        """