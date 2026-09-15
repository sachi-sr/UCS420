roll_no=input("Enter your 8 digit roll number:")
A={int(digit)*7 for digit in roll_no}
B={int(digit)*9 for digit in roll_no}
print ("Set A:",A) 
print("Set B: ",B)
print ("Union of A and B:",A.union(B))
print("Intersection of A and B:",A.intersection(B))

print("A-b:",A.difference(B))
print("B-A:",B.difference(A))

print("Symmetric difference:",A.symmetric_difference(B))
print("Is A a subset of B?",A.issubset(B))
print("Is B a superset of A?",B.issuperset(A))

X=int(input("Enter a value X to remove from A:" ))

A.discard(X)
print("Set A after discarding X:",A)

#discard() is safer because ti does not raise an error if X is not present in the set.