import pandas as pd
import numpy as np

df = pd.read_csv("PyBank/Resources/budget_data.csv")

months = len(df.Date.unique())
total = df["Profit/Losses"].sum()
average = np.diff([df["Profit/Losses"]]).mean()

maxindex = df["Profit/Losses"].idxmax()
maxdate = df["Date"][maxindex]
maxprofit = df["Profit/Losses"][maxindex]

minindex = df["Profit/Losses"].idxmin()
mindate = df["Date"][minindex]
minprofit = df["Profit/Losses"][minindex]

with open("PyBank/bernert_pybank_output.csv",'w') as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------\n")
    f.write(f"Total Months: {months}\n")
    f.write(f"Average Change: {average}\n")
    f.write(f"Greatest Increase in Profits: {maxdate} ${maxprofit}\n")
    f.write(f"Greatest Decrease in Profits: {mindate} ${minprofit}\n")

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {months}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {maxdate} ${maxprofit}")
print(f"Greatest Decrease in Profits: {mindate} ${minprofit}")