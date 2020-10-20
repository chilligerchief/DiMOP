import pandas as pd
from topsis_python import topsis
dataset = pd.read_csv('Topsis_Daten.csv').values
d = dataset[:, 1:]
w = [1, 1, 1, 1]
im = ["-", "+", "+", "-"]
topsis(d,w,im)