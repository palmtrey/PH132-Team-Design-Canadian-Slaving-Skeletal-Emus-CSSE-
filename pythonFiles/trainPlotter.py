import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'traindata.xlsx', index_col = "12 V")

print(data)
