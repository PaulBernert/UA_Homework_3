import pandas as pd

def pypoll():
    df = pd.read_csv("PyPoll/Resources/election_data.csv")
    tot_votes = df.Candidate.count()
    winner = df.groupby('Candidate').count().County.idxmax()
    x = df.Candidate.unique()
    z = df["Candidate"].value_counts()
    y = ((z / tot_votes) * 100).round(2)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {tot_votes}")
    print("-------------------------")
    for i in range(4):
        print(f"{x[i]}: {y[i]}% ({z[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

pypoll()
