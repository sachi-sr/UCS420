# Q2.py

from Assignment2_1 import L
scores = tuple(L[:8])
print("Scores:", scores)
highest=max(scores)
highindex=scores.index(highest)

print("Highest score",highest,"with index",highindex)
lowest=min(scores)
lcount=scores.count(lowest)
print("Lowest score",lowest," no of times it occured",lcount)

reversed_scores=list(scores[::-1])
print("Reversed tuple as list: ",reversed_scores)


user_score=int(input("Enter a score: "))

if user_score in scores:
  print("First occurence index:",scores.index(user_score))
else:
  print("Score is not present in the tuple.")

#scores[0]=100
# GitHub\UCS420\Assignment2_2.py", line 25, in <module>
#     scores[0]=100
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)