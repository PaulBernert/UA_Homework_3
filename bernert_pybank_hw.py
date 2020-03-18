import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PyBank/Resources/budget_data.csv")

maxindex = df["Profit/Losses"].idxmax()
maxdate = df["Date"][maxindex]
maxprofit = df["Profit/Losses"][maxindex]

minindex = df["Profit/Losses"].idxmin()
mindate = df["Date"][minindex]
minprofit = df["Profit/Losses"][minindex]

print(len(df))
print(df["Profit/Losses"].sum())
print(maxdate, maxprofit)
print(mindate, minprofit)

df.plot('Date', 'Profit/Losses')
plt.show()
