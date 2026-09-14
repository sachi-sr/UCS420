from Q1 import df

def score_query(query,df):
  query=query.lower()
  results=[]
  for index, row  in df.iterrows():
    score=0
    keywords = row["keywords"].lower().split()
    for keyword in keywords:
      if keyword in query:
        score+=1
    if score>0:
      results.append((score, row["question"], row["answer"]))
  results.sort(reverse=True)
  return results

query =input("enter your question: ")
results=score_query(query,df)
print("\nmatching FAQs")
for score, question,answer in results:
  print("Confidence ",score)
  print("Question: ",question)
  print("answer ",answer)
  print()