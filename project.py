# ICS 173 final project fall 2022

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

twentytwo_data = pd.read_csv("C:/Users/kneecole/Downloads/ICS 173 final project/Aquaponics Water Quality Tests Data - Log 01_01_2022 - 12_31_2022.csv", index_col="Date:")
twentyone_data = pd.read_csv("C:/Users/kneecole/Downloads/ICS 173 final project/Aquaponics Water Quality Tests Data - Log 01_01_2021 - 12_31_2021.csv", index_col="Date:")
twentyzero_data = pd.read_csv("C:/Users/kneecole/Downloads/ICS 173 final project/Aquaponics Water Quality Tests Data - Log 03_16_2020 - 12_31_2020.csv", index_col="Date:")

plt.figure(figsize=(16,6))
plt.title("Aquaponics data from 2022")
sns.lineplot(data=twentytwo_data)

plt.figure(figsize=(16,6))
plt.title("Aquaponics data from 2021")
sns.lineplot(data=twentyone_data)

plt.figure(figsize=(16,6))
plt.title("Aquaponics data from 2020")
sns.lineplot(data=twentyzero_data)
