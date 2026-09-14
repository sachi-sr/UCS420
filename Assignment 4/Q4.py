from Q1 import df

index = 0

print("Selected FAQ:")
print(df.loc[index])


new_keyword = input("\nEnter a new keyword: ")

df.loc[index, "keywords"] = df.loc[index, "keywords"] + " " + new_keyword

roll_number = "12345623"

filename = roll_number + "_faq_data.csv"

df.to_csv(filename, index=False)

print("\nUpdated FAQ:")
print(df.loc[index])

print("\nDataFrame saved as:", filename)