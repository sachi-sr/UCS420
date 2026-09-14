from Q1 import df

def same_category(category_name, df):

    result = df[df["category"] == category_name]

    return result



personalized_category = df.iloc[4]["category"]

print("Personalized entry category:", personalized_category)

print("\nFAQs belonging to this category:")

print(same_category(personalized_category, df))