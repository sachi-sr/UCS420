import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "Iris.csv"

df = pd.read_csv(file_path)

print("First five rows:")
print(df.head())