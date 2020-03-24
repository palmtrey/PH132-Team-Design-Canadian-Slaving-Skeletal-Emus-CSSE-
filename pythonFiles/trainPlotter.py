import pandas as pd
import matplotlib.pyplot as plt

vavgt12 = pd.read_excel(r"traindataforpython.xlsx", usecols = "A")
vvcorrected12 = pd.read_excel(r"traindataforpython.xlsx", usecols = "B")

print(vavgt12, vvcorrected12)

#times = data.loc[data['12 V']]

plt.plot(vavgt12, vvcorrected12)
plt.show()
