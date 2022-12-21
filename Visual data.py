import pandas as pd
data = pd.read_csv('final_dataset.csv')
from pandas.plotting import scatter_matrix

scatter_matrix(data[['HTGD', 'ATGD', 'HTP', 'ATP', 'DiffLP']], figsize=(12,12))