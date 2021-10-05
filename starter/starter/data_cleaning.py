import pandas as pd

# read the csv file
df = pd.read_csv("data/census.csv")

# remove spaces in column names
df.columns = df.columns.str.replace(' ', '')

print(df.columns)
print(df.info())

# save the new dataset
df.to_csv("data/census_no_spaces.csv", index=False)