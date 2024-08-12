import pandas as pd 
import numpy as np 

moviesDataset = pd.read_csv('../Datasets/movie.csv')

print(moviesDataset)

#The number of empty cells is checked in the data
moviesDataset.replace('(no genres listed)', pd.NA, inplace=True)
empty_check = moviesDataset.iloc[:, 2].isnull().sum()
print(empty_check)
#We found 246 cells are empty

