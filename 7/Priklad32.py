import pandas as pd
import matplotlib.pyplot as plt

# načtu si to od minule...
platy = pd.read_csv('../6/platy_2021_02.csv')

print(platy.head())
rozsah = []
for i in range(30000, 60000, 1000):
    rozsah.append(i)
platy['plat'].hist(bins=rozsah, grid=True )
plt.show()