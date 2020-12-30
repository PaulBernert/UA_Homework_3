import pandas as pd
import numpy as np

def pybank():
    df = pd.read_csv("PyBank/Resources/budget_data.csv")
    months = len(df.Date.unique())
    total = df["Profit/Losses"].sum()
    average = np.diff([df["Profit/Losses"]]).mean()
    maxdate = df["Date"][df["Profit/Losses"].idxmax()]
    maxprofit = df["Profit/Losses"][df["Profit/Losses"].idxmax()]
    mindate = df["Date"][df["Profit/Losses"].idxmin()]
    minprofit = df["Profit/Losses"][df["Profit/Losses"].idxmin()]

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {months}")
    print(f"Average Change: {average}")
    print(f"Greatest Increase in Profits: {maxdate} ${maxprofit}")
    print(f"Greatest Decrease in Profits: {mindate} ${minprofit}")

pybank()
