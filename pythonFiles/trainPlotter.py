import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'traindata.xlsx', index_col = "12 V")

print(data)

times = data.loc[data['12 V']]

plt.plot([1, 2, 3], [1, 2, 3])
plt.show()