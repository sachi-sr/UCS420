from Q1 import df
print("Rows from 3 to 7")
print(df.loc[3:7])
print("Rows 4 to 8 column 2 to 4")
print(df.iloc[4:9,2:5])
print("All rows column 1 to 3")
print(df.iloc[:,1:4])