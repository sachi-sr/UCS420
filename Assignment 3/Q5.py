import pandas as pd 
from pathlib import Path

file_path = Path(__file__).parent / "Iris.csv"
df=pd.read_csv(file_path)

df=df.drop(index=4)

df=df.drop(columns=df.columns[3])

print("After deleting row 4 and column 3:")
print(df)