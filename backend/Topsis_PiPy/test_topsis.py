import pandas as pd
from topsis_python import topsis
dataset = pd.read_csv('data.csv').values
filename = dataset[:, 1:]
weights = [1, 1, 1, 1]
impacts = ["+", "+", "-", "+"]
topsis(filename,weights,impacts)