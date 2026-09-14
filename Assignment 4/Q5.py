from Q1 import df

category_count = df.groupby("category").size()

print("Number of FAQ entries per category:")
print(category_count)